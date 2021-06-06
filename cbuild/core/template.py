# This file provides an interface for a parsed template that is sanitized
# (unlike a raw template, which is just plain python code).
#
# It also provides a reference to what is allowed and what is not.

from re import search
import fnmatch
import shutil
import glob
import sys
import os
import importlib
import pathlib
import contextlib
import subprocess
import shutil
import builtins

from cbuild.core import logger, chroot, paths, xbps
from cbuild import cpu

class PackageError(Exception):
    pass

class SkipPackage(Exception):
    pass

@contextlib.contextmanager
def redir_allout(logpath):
    try:
        pr, pw = os.pipe()
        # save old descriptors
        oldout = os.dup(sys.stdout.fileno())
        olderr = os.dup(sys.stderr.fileno())
        # this will do the logging for us; this way we can get
        # both standard output and file redirection at once
        tee = subprocess.Popen(["tee", logpath], stdin = pr)
        # everything goes into the pipe
        os.dup2(pw, sys.stdout.fileno())
        os.dup2(pw, sys.stderr.fileno())
        # fire
        yield
    finally:
        # restore
        os.dup2(oldout, sys.stdout.fileno())
        os.dup2(olderr, sys.stderr.fileno())
        # close the pipe
        os.close(pw)
        os.close(pr)
        # wait for the tee to finish
        tee.wait()

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
    "pre_fetch": [],
    "do_fetch": [],
    "post_fetch": [],
    "pre_extract": [],
    "do_extract": [],
    "post_extract": [],
    "pre_patch": [],
    "do_patch": [],
    "post_patch": [],
    "pre_configure": [],
    "do_configure": [],
    "post_configure": [],
    "pre_build": [],
    "do_build": [],
    "post_build": [],
    "pre_install": [],
    "do_install": [],
    "post_install": [],
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

class Template(Package):
    def __init__(self, origin):
        super().__init__()

        if origin:
            self.origin = origin
        else:
            self.origin = self

        # mandatory fields
        self.pkgname = None
        self.version = None
        self.revision = None
        self.short_desc = None
        self.homepage = None
        self.license = None
    
        # optional core fields
        self.archs = None
        self.hostmakedepends = []
        self.makedepends = []
        self.depends = []
        self.shlib_provides = None
        self.shlib_requires = None
        self.bootstrap = None
        self.maintainer = None
        self.wrksrc = None
        self.build_wrksrc = ""
        self.create_wrksrc = False
        self.patch_args = None
        self.configure_args = []
        self.make_build_args = []
        self.make_install_args = []
        self.make_build_target = ""
        self.make_install_target = "install"
        self.distfiles = None
        self.checksum = None
        self.skip_extraction = []
        self.subpackages = []
        self.triggers = []
        self.broken = None
        self.nopie = False
        self.noverifyrdeps = False
        self.noshlibprovides = False
        self.skiprdeps = []
        self.shlib_requires = []
        self.shlib_provides = []
        self.make_dirs = []
        self.repository = None
        self.preserve = False
        self.provides = []
        self.replaces = []
        self.conflicts = []
        self.reverts = []
        self.mutable_files = []
        self.conf_files = []
        self.alternatives = []
        self.tags = []
        self.changelog = None
        self.CFLAGS = []
        self.CXXFLAGS = []
        self.LDFLAGS = []
        self.tools = {}
        self.env = {}
    
        # injected
        self.build_style = None
        self.run_depends = None
    
        # other fields
        self.parent = None
        self.rparent = self
        self.subpkg_list = []
        self.source_date_epoch = None

    def ensure_fields(self):
        for f in [
            "pkgname", "version", "revision",
            "short_desc", "homepage", "license"
        ]:
            if not getattr(self, f):
                self.error("missing field: %s" % f)

    def validate_version(self):
        if not isinstance(self.version, str):
            self.error("malformed version field")
        if "-" in self.version:
            self.error("version contains invalid character: -")
        if "_" in self.version:
            self.error("version contains invalid character: _")
        if not search("\d", self.version):
            self.error("version must contain a digit")

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

    def do(self, cmd, args, env = {}, build = False):
        cenv = dict(env);
        cenv["CFLAGS"] = " ".join(self.CFLAGS)
        cenv["CXXFLAGS"] = " ".join(self.CXXFLAGS)
        cenv["LDFLAGS"] = " ".join(self.LDFLAGS)
        cenv["XBPS_TARGET_MACHINE"] = cpu.target()
        cenv["XBPS_MACHINE"] = cpu.host()
        cenv["XBPS_TRIPLET"] = self.triplet
        if self.source_date_epoch:
            cenv["SOURCE_DATE_EPOCH"] = str(self.source_date_epoch)

        cenv.update(self.tools)
        cenv.update(self.env)
        return chroot.enter("/usr/bin/cbuild-do", [
            str(self.chroot_build_wrksrc if build else self.chroot_wrksrc), cmd
        ] + args, env = cenv, check = True)

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

        path = self.abs_wrksrc / path
        dest = self.destdir / dest / path.name

        shutil.copytree(path, dest, symlinks = symlinks)

    def install_dir(self, *args):
        for dn in args:
            dn = pathlib.Path(dn)
            if dn.is_absolute():
                self.logger.out_red(f"path '{str(dn)}' must not be absolute")
                raise PackageError()
            dirp = self.destdir / dn
            self.log(f"creating path: {dirp}")
            os.makedirs(dirp, exist_ok = True)

    def install_bin(self, *args):
        self.install_dir("usr/bin")
        for bn in args:
            spath = self.abs_wrksrc / bn
            dpath = self.destdir / "usr/bin"
            self.log(f"copying (755): {str(spath)} -> {str(dpath)}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o755)

    def install_man(self, *args):
        self.install_dir("usr/share/man")
        manbase = self.destdir / "usr/share/man"
        for mn in args:
            absmn = self.abs_wrksrc / mn
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
            mandir = manbase / ("man" + mnext)
            os.makedirs(mandir, exist_ok = True)
            self.log(f"copying (644): {str(absmn)} -> {str(mandir)}")
            shutil.copy2(absmn, mandir)
            (mandir / mnf).chmod(0o644)

    def install_link(self, src, dest):
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            self.logger.out_red(f"path '{str(dest)}' must not be absolute")
            raise PackageError()
        dest = self.destdir / dest
        self.log(f"symlinking: {str(src)} -> {str(dest)}")
        dest.symlink_to(src)

    def unlink(self, f, root = None):
        f = pathlib.Path(f)
        if f.is_absolute():
            self.logger.out_red(f"path '{str(f)}' must not be absolute")
            raise PackageError()
        remp = (pathlib.Path(root) if root else self.destdir) / f
        self.log(f"removing: {str(remp)}")
        remp.unlink()

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

class Subpackage(Package):
    def __init__(self, name, parent):
        super().__init__()

        self.pkgname = name
        self.parent = parent
        self.rparent = parent

        self.short_desc = parent.short_desc
        self.depends = []
        self.make_dirs = []
        self.noverifyrdeps = False
        self.noshlibprovides = False
        self.skiprdeps = []
        self.shlib_requires = []
        self.shlib_provides = []
        self.repository = parent.repository
        self.preserve = False
        self.provides = []
        self.replaces = []
        self.conflicts = []
        self.reverts = []
        self.mutable_files = []
        self.conf_files = []
        self.alternatives = []
        self.tags = []
        self.triggers = []
        self.changelog = None
        self.run_depends = None

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

def from_module(m, ret):
    # fill in required fields
    ret.pkgname = m.pkgname
    ret.version = m.version
    ret.revision = m.revision
    ret.short_desc = m.short_desc
    ret.homepage = m.homepage
    ret.license = m.license

    # basic validation
    ret.ensure_fields()
    ret.validate_version()

    # this is useful so we don't have to repeat ourselves
    ret.pkgver = f"{ret.pkgname}-{ret.version}_{ret.revision}"

    # other fields
    for fld in [
        "archs", "hostmakedepends", "makedepends", "depends",
        "shlib_provides", "shlib_requires", "bootstrap",
        "maintainer", "wrksrc", "build_wrksrc", "create_wrksrc", "patch_args",
        "configure_args", "make_build_args", "make_install_args",
        "make_build_target", "make_install_target",
        "distfiles", "checksum", "skip_extraction", "subpackages", "triggers",
        "broken", "nopie", "noverifyrdeps", "noshlibprovides", "skiprdeps",
        "shlib_requires", "shlib_provides", "make_dirs", "repository",
        "preserve", "provides", "replaces", "conflicts", "reverts",
        "mutable_files", "conf_files", "alternatives", "tags", "changelog",
        "CFLAGS", "CXXFLAGS", "LDFLAGS", "tools", "env", "build_style"
    ]:
        if hasattr(m, fld):
            setattr(ret, fld, getattr(m, fld))

    if not ret.wrksrc:
        ret.wrksrc = f"{ret.pkgname}-{ret.version}"

    ret.validate_arch()

    # also support build_style via string name for nicer syntax
    if isinstance(ret.build_style, str):
        bs = importlib.import_module("cbuild.build_style." + ret.build_style)
        bs.use(ret)

    # perform initialization (will inject build-style etc)
    if hasattr(m, "init"):
        m.init(ret)

    # add our own methods
    for phase in [
        "fetch", "patch", "extract", "configure", "build", "check", "install"
    ]:
        if hasattr(m, "pre_" + phase):
            setattr(ret, "pre_" + phase, getattr(m, "pre_" + phase))
        if hasattr(m, "do_" + phase):
            setattr(ret, "do_" + phase, getattr(m, "do_" + phase))
        if hasattr(m, "post_" + phase):
            setattr(ret, "post_" + phase, getattr(m, "post_" + phase))

    # paths that can be used by template methods
    ret.files_path = paths.templates() / ret.pkgname / "files"
    ret.chroot_files_path = pathlib.Path("/void-packages/srcpkgs") \
        / ret.pkgname / "files"
    ret.patches_path = paths.templates() / ret.pkgname / "patches"
    ret.builddir = paths.masterdir() / "builddir"
    ret.chroot_builddir = pathlib.Path("/builddir")
    ret.destdir_base = paths.masterdir() / "destdir"
    ret.chroot_destdir_base = pathlib.Path("/destdir")
    ret.destdir = ret.destdir_base / f"{ret.pkgname}-{ret.version}"
    ret.chroot_destdir = ret.chroot_destdir_base / f"{ret.pkgname}-{ret.version}"
    ret.abs_wrksrc = paths.masterdir() / "builddir" / ret.wrksrc
    ret.abs_build_wrksrc = ret.abs_wrksrc / ret.build_wrksrc
    ret.chroot_wrksrc = pathlib.Path("/builddir") \
        / ret.wrksrc
    ret.chroot_build_wrksrc = ret.chroot_wrksrc / ret.build_wrksrc
    ret.statedir = ret.builddir / (".xbps-" + ret.pkgname)
    ret.wrapperdir = ret.statedir / "wrappers"

    ret.env["XBPS_STATEDIR"] = "/builddir/.xbps-" + ret.pkgname

    if not hasattr(ret, "do_install"):
        ret.error("do_install is missing")

    if ret.skip_if_exist:
        # FIXME: this actually uses remote repos too
        bpkgver = xbps.repository_property(ret.pkgname, "pkgver")
        if ret.pkgver == bpkgver:
            if ret.origin == ret:
                # only print if this is not a dependency build
                brepo = xbps.repository_url(ret.pkgname)
                ret.log(f"found ({cpu.target()}) ({brepo})")
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
        sp.pkgver = f"{sp.pkgname}-{ret.version}_{ret.revision}"
        sp.destdir = ret.destdir_base / f"{sp.pkgname}-{ret.version}"
        sp.chroot_destdir = ret.chroot_destdir_base / f"{sp.pkgname}-{ret.version}"
        sp.statedir = ret.statedir
        sp.pkg_install = spf(sp)
        ret.subpkg_list.append(sp)

    if ret.broken:
        ret.log_red("cannot be built, it's currently broken")
        if isinstance(ret.broken, str):
            ret.error(f"{ret.broken}")
        else:
            ret.error(f"yes")

    # try reading the profile
    if not ret.bootstrapping:
        bp = importlib.import_module(
            "cbuild.build_profiles." + cpu.target()
        )
        if not hasattr(bp, "XBPS_TRIPLET"):
            ret.error(f"no target triplet defined")
        ret.triplet = bp.XBPS_TRIPLET
    else:
        bp = importlib.import_module("cbuild.build_profiles.bootstrap")
        ret.triplet = None

    if hasattr(bp, "XBPS_TARGET_CFLAGS"):
        ret.CFLAGS = bp.XBPS_TARGET_CFLAGS + ret.CFLAGS
    if hasattr(bp, "XBPS_TARGET_CXXFLAGS"):
        ret.CXXFLAGS = bp.XBPS_TARGET_CXXFLAGS + ret.CXXFLAGS
    if hasattr(bp, "XBPS_TARGET_LDFLAGS"):
        ret.LDFLAGS = bp.XBPS_TARGET_LDFLAGS + ret.LDFLAGS

    if hasattr(bp, "XBPS_CFLAGS"):
        ret.CFLAGS = bp.XBPS_CFLAGS + ret.CFLAGS
    if hasattr(bp, "XBPS_CXXFLAGS"):
        ret.CXXFLAGS = bp.XBPS_CXXFLAGS + ret.CXXFLAGS
    if hasattr(bp, "XBPS_LDFLAGS"):
        ret.LDFLAGS = bp.XBPS_LDFLAGS + ret.LDFLAGS

    os.makedirs(ret.statedir, exist_ok = True)
    os.makedirs(ret.wrapperdir, exist_ok = True)

    ret.CFLAGS = ["-O2"] + ret.CFLAGS
    ret.CXXFLAGS = ["-O2"] + ret.CXXFLAGS

    if not "CC" in ret.tools:
        ret.tools["CC"] = "cc"
    if not "CXX" in ret.tools:
        ret.tools["CXX"] = "c++"
    if not "CPP" in ret.tools:
        ret.tools["CPP"] = "cpp"
    if not "LD" in ret.tools:
        ret.tools["LD"] = "ld"
    if not "AR" in ret.tools:
        ret.tools["AR"] = "ar"
    if not "AS" in ret.tools:
        ret.tools["AS"] = "as"
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

def read_pkg(pkgname, force_mode, bootstrapping, skip_if_exist, origin):
    if not isinstance(pkgname, str):
        logger.get().out_red("Missing package name.")
        raise PackageError()
    if not (paths.templates() / pkgname / "template").is_file():
        logger.get().out_red("Missing template for '%s'" % cmd[0])
        raise PackageError()

    ret = Template(origin)
    ret.force_mode = force_mode
    ret.bootstrapping = bootstrapping
    ret.skip_if_exist = skip_if_exist

    def subpkg_deco(spkgname):
        def deco(f):
            ret.subpackages.append((spkgname, f))
        return deco

    setattr(builtins, "subpackage", subpkg_deco)
    setattr(builtins, "bootstrapping", bootstrapping)
    mod = importlib.import_module("srcpkgs." + pkgname + ".template")
    delattr(builtins, "subpackage")
    delattr(builtins, "bootstrapping")

    return from_module(mod, ret)

def register_hooks():
    for step in [
        "fetch", "extract", "patch", "configure", "build", "install", "pkg"
    ]:
        for sstep in ["pre", "do", "post"]:
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
