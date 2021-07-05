# This file provides an interface for a parsed template that is sanitized
# (unlike a raw template, which is just plain python code).
#
# It also provides a reference to what is allowed and what is not.

from re import search
import fnmatch
import shutil
import shlex
import time
import glob
import sys
import os
import re
import importlib
import pathlib
import contextlib
import subprocess
import shutil
import builtins

from cbuild.core import logger, chroot, paths, version
from cbuild import cpu

class PackageError(Exception):
    pass

class SkipPackage(Exception):
    pass

@contextlib.contextmanager
def redir_allout(logpath):
    try:
        # save old descriptors
        oldout = os.dup(sys.stdout.fileno())
        olderr = os.dup(sys.stderr.fileno())
        # this will do the logging for us; this way we can get
        # both standard output and file redirection at once
        tee = subprocess.Popen(["tee", logpath], stdin = subprocess.PIPE)
        # everything goes into the pipe
        os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
        os.dup2(tee.stdin.fileno(), sys.stderr.fileno())
        # fire
        yield
    finally:
        # restore
        os.dup2(oldout, sys.stdout.fileno())
        os.dup2(olderr, sys.stderr.fileno())
        # close the pipe
        tee.stdin.close()
        # close the old duplicates
        os.close(oldout)
        os.close(olderr)
        # wait for the tee to finish
        tee.communicate()

# relocate "src" from root "root" to root "dest"
#
# e.g. _submove("foo/bar", "/a", "/b") will move "/b/foo/bar" to "/a/foo/bar"
#
def _submove(src, dest, root):
    dirs = src.parent
    fname = src.name
    ddirs = dest / dirs

    os.makedirs(ddirs, exist_ok = True)

    fsrc = root / src
    fdest = dest / src

    if not fdest.exists():
        shutil.move(fsrc, ddirs)
    else:
        if fdest.is_dir() and fsrc.is_dir():
            # merge the directories
            for fn in fsrc.iterdir():
                _submove(fn.name, fdest, fsrc)
            # remove the source dir that should now be empty
            fsrc.rmdir()
        else:
            raise FileExistsError(f"'{str(fstr)}' and '{str(fdest)}' overlap")

hooks = {
    "init_fetch": [],
    "pre_fetch": [],
    "do_fetch": [],
    "post_fetch": [],
    "init_extract": [],
    "pre_extract": [],
    "do_extract": [],
    "post_extract": [],
    "init_patch": [],
    "pre_patch": [],
    "do_patch": [],
    "post_patch": [],
    "init_configure": [],
    "pre_configure": [],
    "do_configure": [],
    "post_configure": [],
    "init_build": [],
    "pre_build": [],
    "do_build": [],
    "post_build": [],
    "init_install": [],
    "pre_install": [],
    "do_install": [],
    "post_install": [],
    "init_pkg": [],
    "pre_pkg": [],
    "do_pkg": [],
    "post_pkg": []
}

def run_pkg_func(pkg, func, funcn = None, desc = None, on_subpkg = False):
    if not funcn:
        if not hasattr(pkg, func):
            return False
        funcn = func
        
        func = getattr(pkg, funcn)
    if not desc:
        desc = funcn
    if pkg.parent:
        logf = pkg.parent.statedir / f"{pkg.pkgname}__{funcn}.log"
    else:
        logf = pkg.statedir / f"{pkg.pkgname}__{funcn}.log"
    pkg.log(f"running {desc}...")
    with redir_allout(logf):
        if on_subpkg:
            func()
        else:
            func(pkg)
    return True

def call_pkg_hooks(pkg, stepn):
    for f in hooks[stepn]:
        run_pkg_func(pkg, f[0], f"{stepn}_{f[1]}", f"{stepn} hook: {f[1]}")

class Package:
    def __init__(self):
        self.logger = logger.get()
        self.pkgname = None
        self.pkgver = None

    def log(self, msg, end = "\n"):
        self.logger.out(self._get_pv() + ": " + msg, end)

    def log_red(self, msg, end = "\n"):
        self.logger.out_red(self._get_pv() + ": " + msg, end)

    def log_warn(self, msg, end = "\n"):
        self.logger.warn(self._get_pv() + ": " + msg, end)

    def error(self, msg, end = "\n"):
        self.log_red(msg)
        raise PackageError()

    def _get_pv(self):
        if self.pkgver:
            return self.pkgver
        elif self.pkgname:
            return self.pkgname
        return "cbuild"

    def install_files(self, path, dest, symlinks = True):
        path = pathlib.Path(path)
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            self.logger.out_red(
                f"install_files: path '{str(dest)}' must not be absolute"
            )
            raise PackageError()
        if path.is_absolute():
            self.logger.out_red(f"path '{path}' must not be absolute")
            raise PackageError()

        path = self.rparent.abs_wrksrc / path
        dest = self.destdir / dest / path.name

        shutil.copytree(path, dest, symlinks = symlinks)

    def install_dir(self, *args):
        for dn in args:
            dn = pathlib.Path(dn)
            if dn.is_absolute():
                self.logger.out_red(f"path '{str(dn)}' must not be absolute")
                raise PackageError()
            dirp = self.destdir / dn
            if not dirp.is_dir():
                self.log(f"creating path: {dirp}")
                os.makedirs(dirp)

    def install_file(self, src, dest, mode = 0o644, name = None):
        src = pathlib.Path(src)
        dest = pathlib.Path(dest)
        # sanitize destination
        if dest.is_absolute():
            self.logger.out_red(
                f"install_file: path '{str(dest)}' must not be absolute"
            )
            raise PackageError()
        # default name
        if not name:
            name = src.name
        # copy
        dfn = self.destdir / dest / name
        if dfn.exists():
            self.logger.out_red(
                f"install_file: destination file '{str(dfn)}' already exists"
            )
            raise PackageError()
        self.install_dir(dest)
        shutil.copy2(src, dfn)
        dfn.chmod(mode)

    def install_bin(self, *args):
        self.install_dir("usr/bin")
        for bn in args:
            spath = self.rparent.abs_wrksrc / bn
            dpath = self.destdir / "usr/bin"
            self.log(f"copying (755): {str(spath)} -> {str(dpath)}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o755)

    def install_lib(self, *args):
        self.install_dir("usr/lib")
        for bn in args:
            spath = self.rparent.abs_wrksrc / bn
            dpath = self.destdir / "usr/lib"
            self.log(f"copying (755): {str(spath)} -> {str(dpath)}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o755)

    def install_man(self, *args):
        self.install_dir("usr/share/man")
        manbase = self.destdir / "usr/share/man"
        for mn in args:
            absmn = self.rparent.abs_wrksrc / mn
            mnf = absmn.name
            mnext = absmn.suffix
            if len(mnext) == 0:
                self.logger.out_red(f"manpage '{mnf}' has no section")
                raise PackageError()
            try:
                mnsec = int(mnext[1:])
            except:
                self.logger.out_red(f"manpage '{mnf}' has an invalid section")
                raise PackageError()
            mandir = manbase / ("man" + str(mnsec))
            os.makedirs(mandir, exist_ok = True)
            self.log(f"copying (644): {str(absmn)} -> {str(mandir)}")
            shutil.copy2(absmn, mandir)
            (mandir / mnf).chmod(0o644)

    def install_license(self, *args):
        self.install_dir("usr/share/licenses/" + self.pkgname)
        for bn in args:
            spath = self.rparent.abs_wrksrc / bn
            dpath = self.destdir / "usr/share/licenses" / self.pkgname
            self.log(f"copying (644): {str(spath)} -> {str(dpath)}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o644)

    def install_link(self, src, dest):
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            self.logger.out_red(f"path '{str(dest)}' must not be absolute")
            raise PackageError()
        dest = self.destdir / dest
        self.log(f"symlinking: {str(src)} -> {str(dest)}")
        dest.symlink_to(src)

    def copy(self, src, dest, root = None):
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            self.logger.out_red(f"path '{str(dest)}' must not be absolute")
            raise PackageError()
        cp = (pathlib.Path(root) if root else self.destdir) / dest
        self.log(f"copying: {str(src)} -> {str(cp)}")
        shutil.copy2(src, cp)

    def unlink(self, f, root = None, missing_ok = False):
        f = pathlib.Path(f)
        if f.is_absolute():
            self.logger.out_red(f"path '{str(f)}' must not be absolute")
            raise PackageError()
        remp = (pathlib.Path(root) if root else self.destdir) / f
        self.log(f"removing: {str(remp)}")
        remp.unlink(missing_ok)

    def rmtree(self, path, root = None):
        path = pathlib.Path(path)
        if path.is_absolute():
            self.logger.out_red(f"path '{path}' must not be absolute")
            raise PackageError()

        path = (pathlib.Path(root) if root else self.destdir) / path
        if not path.is_dir():
            self.logger.out_red(f"path '{path}' must be a directory")
            raise PackageError()

        def _remove_ro(f, p, _):
            os.chmod(p, stat.S_IWRITE)
            f(p)

        shutil.rmtree(path, onerror = _remove_ro)

    def find(self, pattern, files = False, root = None):
        rootp = pathlib.Path(root if root else self.destdir)
        for fn in rootp.rglob(pattern):
            if not files or fn.is_file():
                yield fn.relative_to(rootp)

core_fields = [
    # name default type optional mandatory subpkg inherit

    # core fields that are set early
    ("pkgname", None, str, False, True, False, False),
    ("version", None, str, False, True, False, False),
    ("revision", None, int, False, True, False, False),
    ("short_desc", None, str, False, True, True, True),
    ("homepage", None, str, False, True, False, False),
    ("license", None, str, False, True, False, False),

    # not mandatory but encouraged
    ("maintainer", None, str, True, False, False, False),

    # other core-ish fields
    ("subpackages", [], list, True, False, False, False),
    ("broken", None, None, True, False, False, False),
    ("build_style", None, str, True, False, False, False),

    # distfiles
    ("distfiles", [], list, True, False, False, False),
    ("checksum", [], list, True, False, False, False),
    ("skip_extraction", [], list, True, False, False, False),

    # target support
    ("archs", None, str, True, False, False, False),
    ("bootstrap", False, bool, False, False, False, False),

    # build directory and patches
    ("wrksrc", None, str, True, False, False, False),
    ("build_wrksrc", "", str, False, False, False, False),
    ("create_wrksrc", False, bool, False, False, False, False),
    ("patch_args", None, str, True, False, False, False),

    # dependency lists
    ("hostmakedepends", [], list, False, False, False, False),
    ("makedepends", [], list, False, False, False, False),
    ("depends", [], list, False, False, True, False),

    # other package lists + related
    ("provides", [], list, False, False, True, False),
    ("conflicts", [], list, False, False, True, False),
    ("skiprdeps", [], list, False, False, True, False),
    ("noverifyrdeps", False, bool, False, False, True, False),

    # build systems
    ("configure_args", [], list, True, False, False, False),
    ("configure_script", "configure", str, False, False, False, False),
    ("make_cmd", "bmake", str, False, False, False, False),
    ("make_build_args", [], list, True, False, False, False),
    ("make_install_args", [], list, True, False, False, False),
    ("make_build_target", "", str, False, False, False, False),
    ("make_install_target", "install", str, False, False, False, False),
    ("disable_parallel_build", False, bool, False, False, False, False),

    # target build related
    ("nodebug", False, bool, False, False, False, False),
    ("nostrip", False, bool, False, False, True, False),
    ("nostrip_files", [], list, False, False, True, False),
    ("hardening", [], list, False, False, True, False),
    ("nopie_files", [], list, False, False, True, False),
    ("tools", {}, dict, False, False, False, False),
    ("env", {}, dict, False, False, False, False),
    ("CFLAGS", [], list, True, False, False, False),
    ("CXXFLAGS", [], list, True, False, False, False),
    ("LDFLAGS", [], list, True, False, False, False),

    # shlibs
    ("shlib_provides", [], list, True, False, True, False),
    ("shlib_requires", [], list, True, False, True, False),
    ("noshlibprovides", False, bool, False, False, True, False),
    ("allow_textrels", False, bool, False, False, False, True),

    # packaging
    ("triggers", [], list, True, False, True, False),
    ("make_dirs", [], list, True, False, True, False),
    ("repository", None, str, True, False, True, True),
    ("conf_files", [], list, True, False, True, False),
    ("tags", [], list, True, False, True, False),
    ("changelog", None, str, True, False, False, False),
]

# recognized hardening options
hardening_fields = {
    "pie": True,
    "ssp": True, # this should really be compiler default
    "scp": False, # stack-clash-protection
}

# for defaults, always make copies
def copy_of_dval(val):
    if isinstance(val, list):
        return list(val)
    if isinstance(val, dict):
        return dict(val)
    return val

class Template(Package):
    def __init__(self, pkgname, origin):
        super().__init__()

        if origin:
            self.origin = origin
        else:
            self.origin = self

        # default all the fields
        for fl, dval, tp, opt, mand, sp, inh in core_fields:
            setattr(self, fl, copy_of_dval(dval))

        # make this available early
        self.pkgname = pkgname

        # other fields
        self.run_depends = None
        self.parent = None
        self.rparent = self
        self.subpkg_list = []
        self.source_date_epoch = None
        self.git_revision = None
        self.git_dirty = False
        self.current_sonames = {}
        self.default_hardening = []

    def setup_reproducible(self):
        self.source_date_epoch = int(time.time())

        if not shutil.which("git"):
            # no git, not reproducible
            return

        tpath = paths.templates() / self.pkgname

        if subprocess.run([
            "git", "rev-parse", "--show-toplevel"
        ], capture_output = True, cwd = tpath).returncode != 0:
            # not in a git repository
            return

        # find whether the template dir has local modifications
        dirty = len(subprocess.run([
            "git", "status", "-s", "--", str(tpath)
        ], capture_output = True).stdout.strip()) != 0

        # find the last revision modifying the template
        self.git_revision = subprocess.run([
            "git", "log", "--format=oneline", "-n1", "--", str(tpath)
        ], capture_output = True).stdout.strip()[0:40].decode("ascii")

        if len(self.git_revision) < 40:
            # ???
            self.git_revision = None
            return

        self.git_dirty = dirty

        # template directory modified, do not use a reproducible date
        if dirty:
            return

        # get the date of the git revision
        ts = subprocess.run([
            "git", "log", "-1", "--format=%cd",
            "--date=unix", self.git_revision
        ], capture_output = True).stdout.strip()

        try:
            self.source_date_epoch = int(ts)
        except ValueError:
            # ???
            pass

    def setup_profile(self, bootstrapping):
        if not bootstrapping:
            bp = importlib.import_module(
                "cbuild.build_profiles." + cpu.target()
            )

            if not hasattr(bp, "CBUILD_TRIPLET"):
                self.error("no target triplet defined")
            if not hasattr(bp, "CBUILD_TARGET_ENDIAN"):
                self.error("no target endianness defined")
            if not hasattr(bp, "CBUILD_TARGET_WORDSIZE"):
                self.error("no target wordsize defined")

            wsize = bp.CBUILD_TARGET_WORDSIZE
            endian = bp.CBUILD_TARGET_ENDIAN

            if wsize != 32 and wsize != 64:
                self.error("invalid CBUILD_TARGET_WORDSIZE value")
            if endian != "little" and endian != "big":
                self.error("invalid CBUILD_TARGET_ENDIAN value")

            if hasattr(bp, "CBUILD_TARGET_HARDENING"):
                self.default_hardening = bp.CBUILD_TARGET_HARDENING

            self.triplet = bp.CBUILD_TRIPLET
            cpu.init_target(wsize, endian)
        else:
            bp = importlib.import_module("cbuild.build_profiles.bootstrap")
            self.triplet = None
            cpu.init_target(cpu.host_wordsize(), cpu.host_endian())

        self.build_profile = bp

    def ensure_fields(self):
        for fl, dval, tp, opt, mand, sp, inh in core_fields:
            # mandatory fields are all at the beginning
            if not mand:
                break
            # basic validation of type
            if not hasattr(self, fl) or not isinstance(getattr(self, fl), tp):
                self.error("missing or invalid field: %s" % fl)

    def validate_version(self):
        try:
            x = version.Version(self.version + "-r" + str(self.revision))
        except:
            self.error("version has an invalid format")

    def validate_arch(self):
        if not self.archs:
            return
        if not isinstance(self.archs, str):
            self.error("malformed archs field")
        archs = self.archs.split()
        matched = False
        for arch in archs:
            negarch = False
            if arch[0] == "~":
                negarch = True
                arch = arch[1:]
            if fnmatch.fnmatchcase(cpu.target(), arch):
                if not negarch:
                    matched = True
                    break
            else:
                if negarch:
                    matched = True
                    break
        if not matched:
            self.error(f"this package cannot be built for {cpu.target()}")

    def parse_hardening(self):
        hdict = dict(hardening_fields)

        for fl in self.default_hardening + self.hardening:
            neg = fl.startswith("!")
            if neg:
                fl = fl[1:]

            if not fl in hdict:
                self.error(f"unrecognized hardening option: {fl}")

            hdict[fl] = not neg

        self.hardening = hdict

    def do(self, cmd, args, env = {}, build = False, wrksrc = None):
        cenv = {
            "CFLAGS": shlex.join(self.CFLAGS),
            "CXXFLAGS": shlex.join(self.CXXFLAGS),
            "LDFLAGS": shlex.join(self.LDFLAGS),
            "CBUILD_TARGET_MACHINE": cpu.target(),
            "CBUILD_MACHINE": cpu.host(),
        }
        if self.source_date_epoch:
            cenv["SOURCE_DATE_EPOCH"] = str(self.source_date_epoch)
        if self.triplet:
            cenv["CBUILD_TRIPLET"] = self.triplet

        cenv.update(self.tools)
        cenv.update(self.env)
        cenv.update(env)

        wdir = self.chroot_build_wrksrc if build else self.chroot_wrksrc
        if wrksrc:
            wdir = wdir / wrksrc

        return chroot.enter(
            str(cmd), args, env = cenv, wrkdir = str(wdir), check = True,
            bootstrapping = self.bootstrapping, ro_root = True,
            mount_distdir = False, unshare_all = True
        )

    def run_step(self, stepn, optional = False, skip_post = False):
        call_pkg_hooks(self, "pre_" + stepn)

        # run pre_* phase
        run_pkg_func(self, "pre_" + stepn)

        # run do_* phase
        if not run_pkg_func(self, "do_" + stepn) and not optional:
            self.error(f"cannot find do_{stepn}")

        call_pkg_hooks(self, "do_" + stepn)

        # run post_* phase
        run_pkg_func(self, "post_" + stepn)

        if not skip_post:
            call_pkg_hooks(self, "post_" + stepn)

class Subpackage(Package):
    def __init__(self, name, parent):
        super().__init__()

        self.pkgname = name
        self.parent = parent
        self.rparent = parent
        self.run_depends = None

        # default subpackage fields
        for fl, dval, tp, opt, mand, sp, inh in core_fields:
            if not sp:
                continue
            if inh:
                setattr(self, fl, copy_of_dval(getattr(parent, fl)))
            else:
                setattr(self, fl, copy_of_dval(dval))

        for fl, dval, tp, opt, sp, inh in parent.build_style_fields:
            if not sp:
                continue
            if inh:
                setattr(self, fl, copy_of_dval(getattr(parent, fl)))
            else:
                setattr(self, fl, copy_of_dval(dval))

        self.force_mode = parent.force_mode
        self.bootstrapping = parent.bootstrapping

    def take(self, *args):
        for p in args:
            p = pathlib.Path(p)
            if p.is_absolute():
                self.logger.out_red(f"path '{p}' must not be absolute")
                raise PackageError()
            origp = self.parent.destdir / p
            got = glob.glob(str(origp))
            if len(got) == 0:
                self.logger.out_red(f"path '{p}' did not match anything")
                raise PackageError()
            for fullp in got:
                # relative path to the file/dir in original destdir
                pdest = self.parent.destdir
                self.log(f"moving: {fullp} -> {str(self.destdir)}")
                _submove(
                    pathlib.Path(fullp).relative_to(pdest), self.destdir, pdest
                )

def _subpkg_install_list(self, l):
    def real_install():
        for it in l:
            self.take(it)

    return real_install

def from_module(m, ret):
    # fill in mandatory fields
    for fl, dval, tp, opt, mand, sp, inh in core_fields:
        # mandatory fields are all at the beginning
        if not mand:
            break
        # no validation for now, that is done later
        if hasattr(m, fl):
            setattr(ret, fl, getattr(m, fl))

    # basic validation
    ret.ensure_fields()
    ret.validate_version()

    # this is useful so we don't have to repeat ourselves
    ret.pkgver = f"{ret.pkgname}-{ret.version}-r{ret.revision}"

    # fill in core non-mandatory fields
    for fl, dval, tp, opt, mand, sp, inh in core_fields:
        # already set
        if mand:
            continue
        # also perform type validation
        if hasattr(m, fl):
            flv = getattr(m, fl)
            if not opt and tp and not isinstance(flv, tp):
                ret.error("invalid field value: %s" % fl)
            # validated, set
            if opt and flv == None:
                setattr(ret, fl, dval)
            else:
                setattr(ret, fl, flv)

    if not ret.wrksrc:
        ret.wrksrc = f"{ret.pkgname}-{ret.version}"

    ret.validate_arch()

    ret.build_style_fields = []

    # also support build_style via string name for nicer syntax
    if isinstance(ret.build_style, str):
        bs = importlib.import_module("cbuild.build_style." + ret.build_style)
        bs.use(ret)

    # perform initialization (will inject build-style etc)
    if hasattr(m, "init"):
        m.init(ret)

    # like above but for build-style specific fields
    for fl, dval, tp, opt, sp, inh in ret.build_style_fields:
        if not hasattr(m, fl):
            setattr(ret, fl, copy_of_dval(dval))
            continue

        flv = getattr(m, fl)
        if not opt and tp and not isinstance(flv, tp):
            ret.error("invalid field value: %s" % fl)
        # validated, set
        if opt and flv == None:
            setattr(ret, fl, dval)
        else:
            setattr(ret, fl, flv)

    # parse hardening fields
    ret.parse_hardening()

    # add our own methods
    for phase in [
        "fetch", "patch", "extract", "configure", "build", "check", "install"
    ]:
        if hasattr(m, "init_" + phase):
            setattr(ret, "init_" + phase, getattr(m, "init_" + phase))
        if hasattr(m, "pre_" + phase):
            setattr(ret, "pre_" + phase, getattr(m, "pre_" + phase))
        if hasattr(m, "do_" + phase):
            setattr(ret, "do_" + phase, getattr(m, "do_" + phase))
        if hasattr(m, "post_" + phase):
            setattr(ret, "post_" + phase, getattr(m, "post_" + phase))

    # pre_pkg from template
    if hasattr(m, "pre_pkg"):
        ret.pre_pkg = m.pre_pkg

    # paths that can be used by template methods
    ret.template_path = paths.templates() / ret.pkgname
    ret.files_path = ret.template_path / "files"
    ret.patches_path = ret.template_path / "patches"
    ret.builddir = paths.masterdir() / "builddir"
    ret.destdir_base = paths.masterdir() / "destdir"
    ret.destdir = ret.destdir_base / f"{ret.pkgname}-{ret.version}"
    ret.abs_wrksrc = paths.masterdir() / "builddir" / ret.wrksrc
    ret.abs_build_wrksrc = ret.abs_wrksrc / ret.build_wrksrc
    ret.statedir = ret.builddir / (".cbuild-" + ret.pkgname)
    ret.wrapperdir = ret.statedir / "wrappers"

    if ret.bootstrapping:
        ret.chroot_builddir = ret.builddir
        ret.chroot_destdir_base = ret.destdir_base
        ret.chroot_wrksrc = ret.abs_wrksrc
        ret.chroot_hostdir = paths.hostdir()
    else:
        ret.chroot_builddir = pathlib.Path("/builddir")
        ret.chroot_destdir_base = pathlib.Path("/destdir")
        ret.chroot_wrksrc = pathlib.Path("/builddir") \
            / ret.wrksrc
        ret.chroot_hostdir = pathlib.Path("/host")

    ret.chroot_build_wrksrc = ret.chroot_wrksrc / ret.build_wrksrc
    ret.chroot_destdir = ret.chroot_destdir_base \
        / f"{ret.pkgname}-{ret.version}"

    ret.env["CBUILD_STATEDIR"] = "/builddir/.cbuild-" + ret.pkgname

    if not hasattr(ret, "do_install"):
        ret.error("do_install is missing")

    if ret.skip_if_exist:
        pinfo = subprocess.run([
            "apk", "search", "-e", "--root", str(paths.masterdir()),
            "--repositories-file", str(paths.hostdir() / "repositories"),
            ret.pkgname
        ], capture_output = True)
        if pinfo.returncode == 0 and len(pinfo.stdout.strip()) > 0:
            if ret.origin == ret:
                # TODO: print the repo somehow
                ret.log(f"found ({pinfo.stdout.strip().decode()})")
            raise SkipPackage()

    spdupes = {}
    # link subpackages and fill in their fields
    for spn, spf in ret.subpackages:
        if spn in spdupes:
            ret.error(f"subpackage '{spn}' already exists")
        spdupes[spn] = True
        sp = Subpackage(spn, ret)
        sp.version = ret.version
        sp.revision = ret.revision
        sp.pkgver = f"{sp.pkgname}-{ret.version}-r{ret.revision}"
        sp.destdir = ret.destdir_base / f"{sp.pkgname}-{ret.version}"
        sp.chroot_destdir = ret.chroot_destdir_base / f"{sp.pkgname}-{ret.version}"
        sp.statedir = ret.statedir
        pinst = spf(sp)
        if not callable(pinst):
            sp.pkg_install = _subpkg_install_list(sp, pinst)
        else:
            sp.pkg_install = pinst
        # validate fields
        for fl, dval, tp, opt, mand, asp, inh in core_fields:
            if not asp:
                continue
            flv = getattr(sp, fl)
            if opt and flv == None:
                continue
            if tp and not isinstance(flv, tp):
                ret.error("invalid field value: %s" % fl)
        # validate build-style fields
        for fl, dval, tp, opt, asp, inh in ret.build_style_fields:
            if not asp:
                continue
            flv = getattr(sp, fl)
            if opt and flv == None:
                continue
            if tp and not isinstance(flv, tp):
                ret.error("invalid field value: %s" % fl)
        # go
        ret.subpkg_list.append(sp)

    if ret.broken:
        ret.log_red("cannot be built, it's currently broken")
        if isinstance(ret.broken, str):
            ret.error(f"{ret.broken}")
        else:
            ret.error(f"yes")

    if hasattr(ret.build_profile, "CBUILD_TARGET_CFLAGS"):
        ret.CFLAGS = ret.build_profile.CBUILD_TARGET_CFLAGS + ret.CFLAGS
    if hasattr(ret.build_profile, "CBUILD_TARGET_CXXFLAGS"):
        ret.CXXFLAGS = ret.build_profile.CBUILD_TARGET_CXXFLAGS + ret.CXXFLAGS
    if hasattr(ret.build_profile, "CBUILD_TARGET_LDFLAGS"):
        ret.LDFLAGS = ret.build_profile.CBUILD_TARGET_LDFLAGS + ret.LDFLAGS

    os.makedirs(ret.statedir, exist_ok = True)
    os.makedirs(ret.wrapperdir, exist_ok = True)

    ret.CFLAGS = ret.base_cflags + ret.CFLAGS
    ret.CXXFLAGS = ret.base_cxxflags + ret.CXXFLAGS
    ret.LDFLAGS = ret.base_ldflags + ret.LDFLAGS

    if not ret.nodebug and ret.build_dbg:
        ret.CFLAGS.append("-g")
        ret.CXXFLAGS.append("-g")

    if not "CC" in ret.tools:
        ret.tools["CC"] = "clang"
    if not "CXX" in ret.tools:
        ret.tools["CXX"] = "clang++"
    if not "CPP" in ret.tools:
        ret.tools["CPP"] = "clang-cpp"
    if not "LD" in ret.tools:
        ret.tools["LD"] = "ld"
    if not "AR" in ret.tools:
        ret.tools["AR"] = "ar"
    if not "AS" in ret.tools:
        ret.tools["AS"] = "clang"
    if not "RANLIB" in ret.tools:
        ret.tools["RANLIB"] = "ranlib"
    if not "STRIP" in ret.tools:
        ret.tools["STRIP"] = "strip"
    if not "OBJDUMP" in ret.tools:
        ret.tools["OBJDUMP"] = "objdump"
    if not "OBJCOPY" in ret.tools:
        ret.tools["OBJCOPY"] = "objcopy"
    if not "NM" in ret.tools:
        ret.tools["NM"] = "nm"
    if not "READELF" in ret.tools:
        ret.tools["READELF"] = "readelf"
    if not "PKG_CONFIG" in ret.tools:
        ret.tools["PKG_CONFIG"] = "pkg-config"

    return ret

_tmpl_dict = {}

def read_pkg(
    pkgname, force_mode, bootstrapping, skip_if_exist, build_dbg,
    cflags, cxxflags, ldflags, origin
):
    global _tmpl_dict

    if not isinstance(pkgname, str):
        logger.get().out_red("Missing package name.")
        raise PackageError()

    if not (paths.templates() / pkgname / "template.py").is_file():
        logger.get().out_red("Missing template for '%s'" % pkgname)
        raise PackageError()

    ret = Template(pkgname, origin)
    ret.force_mode = force_mode
    ret.bootstrapping = bootstrapping
    ret.skip_if_exist = skip_if_exist
    ret.build_dbg = build_dbg
    ret.cross_build = False
    ret.base_cflags = cflags
    ret.base_cxxflags = cxxflags
    ret.base_ldflags = ldflags

    ret.setup_reproducible()
    ret.setup_profile(bootstrapping)

    def subpkg_deco(spkgname):
        def deco(f):
            ret.subpackages.append((spkgname, f))
        return deco

    setattr(builtins, "subpackage", subpkg_deco)
    setattr(builtins, "current", ret)

    modh = _tmpl_dict.get(pkgname, None)
    if modh:
        # clear all user set fields since reload retains them
        for fld in dir(modh):
            # don't mess with the internals
            if fld.startswith("__") and fld.endswith("__"):
                continue
            delattr(modh, fld)
        # now reload
        modh = importlib.reload(modh)
    else:
        # never loaded
        modh = importlib.import_module("srcpkgs." + pkgname + ".template")

    _tmpl_dict[pkgname] = modh

    delattr(builtins, "current")
    delattr(builtins, "subpackage")

    return from_module(modh, ret)

def register_hooks():
    for step in [
        "fetch", "extract", "patch", "configure", "build", "install", "pkg"
    ]:
        for sstep in ["init", "pre", "do", "post"]:
            stepn = f"{sstep}_{step}"
            dirn = paths.cbuild() / "hooks" / stepn
            if dirn.is_dir():
                for f in dirn.glob("*.py"):
                    # this must be skipped
                    if f.name == "__init__.py":
                        continue
                    modn = "cbuild.hooks." + stepn + "." + f.stem
                    modh = importlib.import_module(modn)
                    if not hasattr(modh, "invoke"):
                        logger.get().out_red(
                            f"Hook '{stepn}/{f.stem}' does not have an entry point."
                        )
                        raise Exception()
                    hooks[stepn].append((modh.invoke, f.stem))
