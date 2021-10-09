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
import configparser

from cbuild.core import logger, chroot, paths, profile, spdx
from cbuild.apk import cli

class PackageError(Exception):
    pass

class SkipPackage(Exception):
    pass

class StampException(BaseException):
    pass

class StampCheck:
    def __init__(self, pkg, name):
        self.pkg = pkg
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exct, excv, tback):
        if not exct:
            (self.pkg.cwd / f".stamp_{self.name}_done").touch()
            return True

        return isinstance(excv, StampException)

    def check(self):
        if (self.pkg.cwd / f".stamp_{self.name}_done").exists():
            raise StampException()

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

    ddirs.mkdir(parents = True, exist_ok = True)

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
            raise FileExistsError(f"'{fsrc}' and '{fdest}' overlap")

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
    "init_check": [],
    "pre_check": [],
    "do_check": [],
    "post_check": [],
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
    crossb = pkg.rparent.cross_build if pkg.rparent.cross_build else ""
    if pkg.parent:
        logf = pkg.parent.statedir / f"{pkg.pkgname}_{crossb}_{funcn}.log"
    else:
        logf = pkg.statedir / f"{pkg.pkgname}_{crossb}_{funcn}.log"
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
        if self.pkgname and self.pkgver:
            return f"{self.pkgname}-{self.pkgver}-r{self.pkgrel}"
        elif self.pkgname:
            return self.pkgname
        return "cbuild"

    @contextlib.contextmanager
    def pushd(self, dirn):
        old_path = self.rparent.cwd
        old_cpath = self.rparent.chroot_cwd

        new_path = old_path / dirn

        if not new_path.is_dir():
            self.error(f"path '{new_path}' is not a directory")

        new_path = new_path.resolve()

        self.rparent.cwd = new_path
        self.rparent.chroot_cwd = pathlib.Path("/") / new_path.relative_to(
            paths.bldroot()
        )

        try:
            yield
        finally:
            self.rparent.cwd = old_path
            self.rparent.chroot_cwd = old_cpath

    def cp(self, srcp, destp, recursive = False, symlinks = True):
        srcp = self.rparent.cwd / srcp
        destp = self.rparent.cwd / destp

        if recursive and srcp.is_dir():
            if destp.is_dir():
                destp = destp / srcp.name
            if srcp.is_symlink():
                ret = shutil.copy2(srcp, destp, follow_symlinks = False)
            else:
                ret = shutil.copytree(
                    srcp, destp, symlinks = symlinks, dirs_exist_ok = True
                )
        elif srcp.is_dir():
            self.error(f"'{srcp}' is a directory, but not using 'recursive'")
        else:
            ret = shutil.copy2(srcp, destp, follow_symlinks = symlinks)

        return pathlib.Path(ret)

    def mv(self, srcp, destp):
        srcp = self.rparent.cwd / srcp
        destp = self.rparent.cwd / destp

        return pathlib.Path(shutil.move(srcp, destp))

    def mkdir(self, path, parents = False):
        (self.rparent.cwd / path).mkdir(parents = parents, exist_ok = parents)

    def rm(self, path, recursive = False, force = False):
        path = self.rparent.cwd / path

        if not recursive:
            if path.is_dir() and not path.is_symlink():
                self.error(f"'{path}' is a directory")
            path.unlink(missing_ok = force)
        else:
            def _remove_ro(f, p, _):
                os.chmod(p, stat.S_IWRITE)
                f(p)

            if force and not path.exists():
                return

            if not path.is_dir() or path.is_symlink():
                path.unlink(missing_ok = force)
            else:
                shutil.rmtree(path, onerror = _remove_ro)

    def ln_s(self, srcp, destp, relative = False):
        destp = self.rparent.cwd / destp
        if destp.is_dir():
            destp = destp / pathlib.Path(srcp).name
        if relative:
            srcp = os.path.relpath(srcp, start = destp)
        destp.symlink_to(srcp)

    def chmod(self, path, mode):
        (self.rparent.cwd / path).chmod(mode)

    def find(self, path, pattern, files = False):
        path = pathlib.Path(path)
        if path.is_absolute():
            for fn in path.rglob(pattern):
                if not files or fn.is_file():
                    yield fn
        else:
            cwp = self.rparent.cwd
            path = cwp / path
            for fn in path.rglob(pattern):
                if not files or fn.is_file():
                    yield fn.relative_to(cwp)

default_options = {
    #           default inherit
    "bootstrap": (False, True),
    "checkroot": (False, True),
    "keepempty": (False, False),
    "brokenlinks": (False, False),
    "scanrundeps": (True, False),
    "scanshlibs": (True, False),
    "scanpkgconf": (True, False),
    "scancmd": (True, False),
    "textrels": (False, True),
    "parallel": (True, True),
    "debug": (True, True),
    "strip": (True, False),
    "check": (True, True),
    "cross": (True, True),
    "lint": (True, False),
    "spdx": (True, False),
}

core_fields = [
    # name default type mandatory subpkg inherit

    # core fields that are set early
    ("license", None, str, True, False, False),
    ("pkgdesc", None, str, True, True, True),
    ("pkgname", None, str, True, False, False),
    ("pkgrel", None, int, True, False, False),
    ("pkgver", None, str, True, False, False),
    ("url", None, str, True, False, False),

    # not mandatory but encouraged
    ("maintainer", None, str, False, False, False),

    # various options that can be set for the template
    ("options", [], list, False, True, False),

    # other core-ish fields
    ("subpackages", [], list, False, False, False),
    ("broken", None, str, False, False, False),
    ("build_style", None, str, False, False, False),

    # sources
    ("sha256", [], list, False, False, False),
    ("sources", [], list, False, False, False),

    # target support
    ("archs", None, str, False, False, False),

    # build directory and patches
    ("build_wrksrc", "", str, False, False, False),
    ("patch_args", [], list, False, False, False),

    # dependency lists
    ("checkdepends", [], list, False, False, False),
    ("hostmakedepends", [], list, False, False, False),
    ("makedepends", [], list, False, False, False),
    ("depends", [], list, False, True, False),

    # other package lists + related
    ("provides", [], list, False, True, False),

    # build systems
    ("configure_args", [], list, False, False, False),
    ("configure_script", "configure", str, False, False, False),
    ("make_cmd", "bmake", str, False, False, False),
    ("make_dir", ".", str, False, False, False),
    ("make_build_args", [], list, False, False, False),
    ("make_install_args", [], list, False, False, False),
    ("make_check_args", [], list, False, False, False),
    ("make_build_target", "", str, False, False, False),
    ("make_install_target", "install", str, False, False, False),
    ("make_check_target", "check", str, False, False, False),

    # target build related
    ("nostrip_files", [], list, False, True, False),
    ("hardening", [], list, False, True, False),
    ("nopie_files", [], list, False, True, False),
    ("suid_files", [], list, False, True, False),
    ("tools", {}, dict, False, False, False),
    ("tool_flags", {}, dict, False, False, False),
    ("env", {}, dict, False, False, False),
    ("debug_level", 2, int, False, False, False),

    # packaging
    ("triggers", [], list, False, True, False),
]

# recognized hardening options
hardening_fields = {
    "fortify": True,
    "pie": True,
    "ssp": True, # this should really be compiler default
    "scp": False, # stack-clash-protection
}

cross_tools = {
    "CC": True,
    "CXX": True,
    "CPP": True,
    "LD": True,
    "PKG_CONFIG": True,
}

# for defaults, always make copies
def copy_of_dval(val):
    if isinstance(val, list):
        return list(val)
    if isinstance(val, dict):
        return dict(val)
    return val

def pkg_profile(pkg, target):
    if pkg.bootstrapping and (target == "host" or target == "target"):
        return profile.get_profile("bootstrap")
    elif target == "host":
        return profile.get_profile(chroot.host_cpu())
    elif target == "target":
        return profile.get_profile(chroot.target_cpu())
    elif not target:
        return pkg.build_profile

    return profile.get_profile(target)

class Template(Package):
    def __init__(self, pkgname, origin):
        super().__init__()

        if origin:
            self.origin = origin
        else:
            self.origin = self

        # default all the fields
        for fl, dval, tp, mand, sp, inh in core_fields:
            setattr(self, fl, copy_of_dval(dval))

        # make this available early
        self.repository, self.pkgname = pkgname.split("/")

        # resolve all source repos available to this package
        self.source_repositories = [self.repository]
        crepo = self.repository
        # the toplevel repo is already added
        while True:
            # check if the current repo has a parent link
            rp = paths.distdir() / crepo / ".parent"
            if not rp.is_symlink():
                break
            # try resolving it, if it resolves, consider it
            try:
                rp = rp.readlink()
            except:
                break
            # it resolved, consider the name
            crepo = rp.name
            # skip if it does not resolve to a repository
            if not (paths.distdir() / crepo).is_dir():
                break
            # append and repeat
            self.source_repositories.append(crepo)

        # other fields
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

        if subprocess.run([
            "git", "rev-parse", "--show-toplevel"
        ], capture_output = True, cwd = self.template_path).returncode != 0:
            # not in a git repository
            return

        # find whether the template dir has local modifications
        dirty = len(subprocess.run([
            "git", "status", "-s", "--", self.template_path
        ], capture_output = True).stdout.strip()) != 0

        # find the last revision modifying the template
        self.git_revision = subprocess.run([
            "git", "log", "--format=oneline", "-n1", "--", self.template_path
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

    def ensure_fields(self):
        for fl, dval, tp, mand, sp, inh in core_fields:
            # mandatory fields are all at the beginning
            if not mand:
                break
            # basic validation of type
            if not hasattr(self, fl) or not isinstance(getattr(self, fl), tp):
                self.error("missing or invalid field: %s" % fl)

    def validate_pkgver(self):
        if not cli.check_version(f"{self.pkgver}-r{self.pkgrel}"):
            self.error("pkgver has an invalid format")

    def validate_pkgdesc(self):
        # do not validate if not linting
        if not self.options["lint"]:
            return

        dstr = self.pkgdesc
        if re.search(r"\.$", dstr):
            self.error("pkgdesc should not end with a period")
        if re.search(r"\s$", dstr):
            self.error("pkgdesc should not end with whitespace")
        if re.search(r"^\s", dstr):
            self.error("pkgdesc should not start with whitespace")
        if re.search(r"\s$", dstr):
            self.error("pkgdesc should not end with whitespace")
        if re.search(r"^(An?|The) ", dstr):
            self.error("pkgdesc should not start with an article")
        if re.search(r"^[a-z]", dstr):
            self.error("pkgdesc should start with an uppercase letter")
        if len(dstr) > 72:
            self.error("pkgdesc should be no longer than 72 characters")

    def validate_arch(self):
        bprof = self.build_profile
        archn = bprof.arch
        # no archs specified: we match always
        if not self.archs:
            return
        # bad archs type
        if not isinstance(self.archs, list):
            self.error("malformed archs field")
        # find matching patterns; pattern matching the arch name more exactly
        # (i.e. having more non-pattern characters) trumps the previous one
        prevmatch = None
        prevneg = False
        # function to find number of exact chars in both patterns
        def _find_exact(s):
            i = 0
            ret = 0
            while i < len(s):
                if s[i] == "*" or s[i] == "?":
                    i += 1
                    continue
                if s[i] == "[":
                    while i < len(s) and s[i] != "]":
                        i += 1
                    if i == len(s):
                        break
                    i += 1
                    continue
                ret += 1
                i += 1
            return ret
        # now match
        for v in self.archs:
            # negative match pattern: acknowledge and get the pattern
            curneg = v.startswith("!")
            if curneg:
                v = v[1:]
            # if not a match, skip
            if not fnmatch.fnmatchcase(archn, v):
                continue
            # no previous reference pattern
            if not prevmatch:
                prevmatch = v
                prevneg = curneg
                continue
            # equal patterns: skip
            if v == prevmatch:
                if prevneg != curneg:
                    self.error(f"conflicting arch patterns: {v}, !{v}")
                continue
            # find the non-pattern lengths
            nexactprev = _find_exact(prevmatch)
            nexactcur = _find_exact(v)
            # same number of exactly matched characters is ambiguous
            if nexactcur == nexactprev:
                if prevneg:
                    prevmatch = f"!{prevmatch}"
                if curneg:
                    v = f"!{v}"
                self.error(f"ambiguous arch patterns: {prevmatch}, {v}")
            # otherwise consider the one with longer exact match
            if nexactcur > nexactprev:
                prevmatch = v
                prevneg = curneg
        # no match or negative match
        if not prevmatch or prevneg:
            self.error(f"this package cannot be built for {archn}")
        # otherwise we're good

    def do(self, cmd, args, env = {}, wrksrc = None):
        cenv = {
            "CBUILD_TARGET_MACHINE": self.build_profile.arch,
            "CBUILD_HOST_MACHINE": chroot.host_cpu(),
        }

        fakestrip = self.wrapperdir / "strip"
        if not self.bootstrapping:
            fakestrip = pathlib.Path("/builddir") / \
                fakestrip.relative_to(self.builddir)

        cenv["STRIPBIN"] = str(fakestrip)

        # cflags and so on
        for k in self.tool_flags:
            cenv[k] = self.get_tool_flags(k, shell = True)

        if self.source_date_epoch:
            cenv["SOURCE_DATE_EPOCH"] = str(self.source_date_epoch)
        if self.build_profile.triplet:
            cenv["CBUILD_TARGET_TRIPLET"] = self.build_profile.triplet

        if self.use_ccache:
            cenv["CCACHEPATH"] = "/usr/lib/ccache/bin"
            cenv["CCACHE_DIR"] = "/ccache"
            cenv["CCACHE_COMPILERCHECK"] = "content"
            cenv["CCACHE_COMPRESS"] = "1"
            cenv["CCACHE_BASEDIR"] = str(self.chroot_cwd)

        cenv.update(self.tools)

        cenv["CC"] = self.get_tool("CC")
        cenv["CXX"] = self.get_tool("CXX")
        cenv["CPP"] = self.get_tool("CPP")
        cenv["LD"] = self.get_tool("LD")
        cenv["PKG_CONFIG"] = self.get_tool("PKG_CONFIG")

        with self.profile("host"):
            cenv["BUILD_CC"] = self.get_tool("CC")
            cenv["BUILD_CXX"] = self.get_tool("CXX")
            cenv["BUILD_CPP"] = self.get_tool("CPP")
            cenv["BUILD_LD"] = self.get_tool("LD")
            cenv["BUILD_PKG_CONFIG"] = self.get_tool("PKG_CONFIG")

            # cflags and so on
            for k in self.tool_flags:
                cenv["BUILD_" + k] = self.get_tool_flags(k, shell = True)

            if self.build_profile.triplet:
                cenv["CBUILD_HOST_TRIPLET"] = self.build_profile.triplet

        cenv.update(self.env)
        cenv.update(env)

        wdir = self.chroot_cwd
        if wrksrc:
            wdir = wdir / wrksrc

        puid = None
        if self.current_phase == "install":
            puid = 0
        elif self.current_phase == "check" and self.options["checkroot"]:
            puid = 0

        return chroot.enter(
            cmd, args, env = cenv, wrkdir = wdir, check = True,
            bootstrapping = self.bootstrapping, ro_root = True,
            ro_build = self.install_done,
            ro_dest = (self.current_phase != "install"),
            mount_ccache = True, unshare_all = (self.current_phase != "fetch"),
            pretend_uid = puid, pretend_gid = puid
        )

    def stamp(self, name):
        return StampCheck(self, name)

    def run_step(self, stepn, optional = False, skip_post = False):
        # reinit to make sure we've got up to date info
        chroot.set_target(self.build_profile.arch)

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

    def get_tool_flags(
        self, name, extra_flags = [], hardening = [],
        shell = False, target = None
    ):
        target = pkg_profile(self, target)

        if name in self.tool_flags:
            tfb = self.tool_flags[name] + extra_flags
        else:
            tfb = extra_flags

        dodbg = self.build_dbg and self.options["debug"]

        return target.get_tool_flags(
            name, tfb,
            self.debug_level if dodbg else -1,
            self.hardening + hardening,
            shell = shell
        )

    def get_cflags(
        self, extra_flags = [], hardening = [], shell = False, target = None
    ):
        return self.get_tool_flags(
            "CFLAGS", extra_flags, hardening, shell, target
        )

    def get_cxxflags(
        self, extra_flags = [], hardening = [], shell = False, target = None
    ):
        return self.get_tool_flags(
            "CXXFLAGS", extra_flags, hardening, shell, target
        )

    def get_fflags(
        self, extra_flags = [], hardening = [], shell = False, target = None
    ):
        return self.get_tool_flags(
            "FFLAGS", extra_flags, hardening, shell, target
        )

    def get_ldflags(
        self, extra_flags = [], hardening = [], shell = False, target = None
    ):
        return self.get_tool_flags(
            "LDFLAGS", extra_flags, hardening, shell, target
        )

    def get_tool(self, name, target = None):
        if not name in self.tools:
            return None

        target = pkg_profile(self, target)

        if name in cross_tools and target.cross:
            # special case for cross toolchains
            if not self.pkgname.endswith("-cross"):
                return f"{target.short_triplet}-{self.tools[name]}"

        return self.tools[name]

    def has_hardening(self, hname, target = None):
        target = pkg_profile(self, target)

        return target.has_hardening(hname, self.hardening)

    @contextlib.contextmanager
    def profile(self, target):
        old_tgt = self.build_profile

        if self.bootstrapping and (target == "host" or target == "target"):
            target = "bootstrap"
        elif target == "host":
            target = chroot.host_cpu()
        elif target == "target":
            target = chroot.target_cpu()

        try:
            self.build_profile = profile.get_profile(target)
            yield
        finally:
            self.build_profile = old_tgt

    def install_files(self, path, dest, symlinks = True):
        path = pathlib.Path(path)
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            self.logger.out_red(
                f"install_files: path '{dest}' must not be absolute"
            )
            raise PackageError()
        if path.is_absolute():
            self.logger.out_red(f"path '{path}' must not be absolute")
            raise PackageError()

        path = self.cwd / path
        dest = self.destdir / dest / path.name

        shutil.copytree(path, dest, symlinks = symlinks)

    def install_dir(self, *args):
        for dn in args:
            dn = pathlib.Path(dn)
            if dn.is_absolute():
                self.logger.out_red(f"path '{dn}' must not be absolute")
                raise PackageError()
            dirp = self.destdir / dn
            if not dirp.is_dir():
                self.log(f"creating path: {dirp}")
                dirp.mkdir(parents = True)

    def install_file(self, src, dest, mode = 0o644, name = None):
        src = pathlib.Path(src)
        dest = pathlib.Path(dest)
        # sanitize destination
        if dest.is_absolute():
            self.logger.out_red(
                f"install_file: path '{dest}' must not be absolute"
            )
            raise PackageError()
        # default name
        if not name:
            name = src.name
        # copy
        dfn = self.destdir / dest / name
        if dfn.exists():
            self.logger.out_red(
                f"install_file: destination file '{dfn}' already exists"
            )
            raise PackageError()
        self.install_dir(dest)
        shutil.copy2(self.cwd / src, dfn)
        if mode != None:
            dfn.chmod(mode)

    def install_bin(self, *args):
        self.install_dir("usr/bin")
        for bn in args:
            spath = self.cwd / bn
            dpath = self.destdir / "usr/bin"
            self.log(f"copying (755): {spath} -> {dpath}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o755)

    def install_lib(self, *args):
        self.install_dir("usr/lib")
        for bn in args:
            spath = self.cwd / bn
            dpath = self.destdir / "usr/lib"
            self.log(f"copying (755): {spath} -> {dpath}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o755)

    def install_man(self, *args):
        self.install_dir("usr/share/man")
        manbase = self.destdir / "usr/share/man"
        for mn in args:
            absmn = self.cwd / mn
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
            mandir = manbase / f"man{mnsec}"
            mandir.mkdir(parents = True, exist_ok = True)
            self.log(f"copying (644): {absmn} -> {mandir}")
            shutil.copy2(absmn, mandir)
            (mandir / mnf).chmod(0o644)

    def install_license(self, *args):
        self.install_dir("usr/share/licenses/" + self.pkgname)
        for bn in args:
            spath = self.cwd / bn
            dpath = self.destdir / "usr/share/licenses" / self.pkgname
            self.log(f"copying (644): {spath} -> {dpath}")
            shutil.copy2(spath, dpath)
            (dpath / spath.name).chmod(0o644)

    def install_link(self, src, dest):
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            self.logger.out_red(f"path '{dest}' must not be absolute")
            raise PackageError()
        dest = self.destdir / dest
        self.log(f"symlinking: {src} -> {dest}")
        dest.symlink_to(src)

class Subpackage(Package):
    def __init__(self, name, parent):
        super().__init__()

        self.pkgname = name
        self.parent = parent
        self.rparent = parent

        # default subpackage fields
        for fl, dval, tp, mand, sp, inh in core_fields:
            if not sp:
                continue
            if inh:
                setattr(self, fl, copy_of_dval(getattr(parent, fl)))
            else:
                setattr(self, fl, copy_of_dval(dval))

        for fl, dval, tp, sp, inh in parent.build_style_fields:
            if not sp:
                continue
            if inh:
                setattr(self, fl, copy_of_dval(getattr(parent, fl)))
            else:
                setattr(self, fl, copy_of_dval(dval))

        ddeps = []
        bdep = None

        # default suffixes
        if name.endswith("-devel"):
            self.pkgdesc += " (development files)"
        elif name.endswith("-doc"):
            self.pkgdesc += " (documentation)"
            bdep = name.removesuffix("-doc")
        elif name.endswith("-libs"):
            self.pkgdesc += " (libraries)"
        elif name.endswith("-dbg"):
            self.pkgdesc += " (debug files)"
            bdep = name.removesuffix("-dbg")
        elif name.endswith("-progs"):
            self.pkgdesc += " (programs)"

        # by default some subpackages depeond on their parent package
        if bdep:
            ddeps.append(f"{bdep}={parent.pkgver}-r{parent.pkgrel}")

        self.depends = ddeps

        self.force_mode = parent.force_mode
        self.bootstrapping = parent.bootstrapping

    def take(self, p, missing_ok = False):
        p = pathlib.Path(p)
        if p.is_absolute():
            self.logger.out_red(f"path '{p}' must not be absolute")
            raise PackageError()
        origp = self.parent.destdir / p
        got = glob.glob(str(origp))
        if len(got) == 0 and not missing_ok:
            self.logger.out_red(f"path '{p}' did not match anything")
            raise PackageError()
        for fullp in got:
            # relative path to the file/dir in original destdir
            pdest = self.parent.destdir
            self.log(f"moving: {fullp} -> {self.destdir}")
            _submove(
                pathlib.Path(fullp).relative_to(pdest), self.destdir, pdest
            )

    def take_devel(self):
        self.take("usr/bin/*-config", missing_ok = True)
        self.take("usr/lib/*.a", missing_ok = True)
        self.take("usr/lib/*.so", missing_ok = True)
        self.take("usr/lib/pkgconfig", missing_ok = True)
        self.take("usr/lib/cmake", missing_ok = True)
        self.take("usr/lib/glade/modules", missing_ok = True)
        self.take("usr/include", missing_ok = True)
        self.take("usr/share/cmake", missing_ok = True)
        self.take("usr/share/pkgconfig", missing_ok = True)
        self.take("usr/share/aclocal", missing_ok = True)
        self.take("usr/share/gettext", missing_ok = True)
        self.take("usr/share/vala/vapi", missing_ok = True)
        self.take("usr/share/gir-[0-9]*", missing_ok = True)
        self.take("usr/share/glade/catalogs", missing_ok = True)

    def take_doc(self):
        self.take("usr/share/doc", missing_ok = True)
        self.take("usr/share/man", missing_ok = True)
        self.take("usr/share/info", missing_ok = True)
        self.take("usr/share/html", missing_ok = True)
        self.take("usr/share/licenses", missing_ok = True)
        self.take("usr/share/sgml", missing_ok = True)
        self.take("usr/share/gtk-doc", missing_ok = True)
        self.take("usr/share/ri", missing_ok = True)
        self.take("usr/share/help", missing_ok = True)

    def take_libs(self):
        self.take("usr/lib/lib*.so.[0-9]*")

    def take_progs(self):
        self.take("usr/bin/*")

    def default_devel(self):
        return lambda: self.take_devel()

    def default_doc(self):
        return lambda: self.take_devel()

    def default_libs(self):
        return lambda: self.take_libs()

    def default_progs(self):
        return lambda: self.take_progs()

def _subpkg_install_list(self, l):
    def real_install():
        for it in l:
            self.take(it)

    return real_install

def from_module(m, ret):
    # fill in mandatory fields
    for fl, dval, tp, mand, sp, inh in core_fields:
        # mandatory fields are all at the beginning
        if not mand:
            break
        # no validation for now, that is done later
        if hasattr(m, fl):
            setattr(ret, fl, getattr(m, fl))

    # basic validation
    ret.ensure_fields()
    ret.validate_pkgver()

    # fill in core non-mandatory fields
    for fl, dval, tp, mand, sp, inh in core_fields:
        # already set
        if mand:
            continue
        # also perform type validation
        if hasattr(m, fl):
            flv = getattr(m, fl)
            if tp and not isinstance(flv, tp):
                ret.error("invalid field value: %s" % fl)
            # validated, set
            setattr(ret, fl, flv)

    # transform options
    ropts = {}

    for dopt, dtup in default_options.items():
        ropts[dopt] = dtup[0]

    if ret.options:
        for opt in ret.options:
            neg = opt.startswith("!")
            if neg:
                opt = opt[1:]
            if not opt in ropts:
                ret.error("unknown option: %s" % opt)
            ropts[opt] = not neg

    ret.options = ropts
    ret.wrksrc = f"{ret.pkgname}-{ret.pkgver}"

    ret.validate_arch()
    ret.validate_pkgdesc()

    # validate license if we need to
    if ret.options["spdx"]:
        lerr = None
        try:
            spdx.validate(ret.license)
        except RuntimeError as e:
            lerr = str(e)
        if lerr:
            ret.error("failed validating license: %s" % lerr)

    # the real job count
    if not ret.options["parallel"]:
        ret.make_jobs = 1
    else:
        ret.make_jobs = ret.conf_jobs

    ret.build_style_fields = []
    ret.build_style_defaults = []

    if ret.build_style:
        importlib.import_module(f"cbuild.build_style.{ret.build_style}").use(ret)

    # perform initialization
    if hasattr(m, "init"):
        m.init(ret)

    # like above but for build-style specific fields
    for fl, dval, tp, sp, inh in ret.build_style_fields:
        if not hasattr(m, fl):
            setattr(ret, fl, copy_of_dval(dval))
            continue

        flv = getattr(m, fl)
        if tp and not isinstance(flv, tp):
            ret.error("invalid field value: %s" % fl)
        # validated, set
        setattr(ret, fl, flv)

    # set default fields for build_style if not set by template
    for fl, dval in ret.build_style_defaults:
        if not hasattr(m, fl):
            setattr(ret, fl, copy_of_dval(dval))

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
    ret.files_path = ret.template_path / "files"
    ret.patches_path = ret.template_path / "patches"
    ret.builddir = paths.bldroot() / "builddir"
    ret.statedir = ret.builddir / (".cbuild-" + ret.pkgname)
    ret.wrapperdir = ret.statedir / "wrappers"

    if ret.build_profile.cross:
        ret.destdir_base = paths.bldroot() / "destdir" / \
            ret.build_profile.triplet
    else:
        ret.destdir_base = paths.bldroot() / "destdir"

    ret.destdir = ret.destdir_base / f"{ret.pkgname}-{ret.pkgver}"

    ret.cwd = ret.builddir / ret.wrksrc / ret.build_wrksrc

    if ret.bootstrapping:
        ret.chroot_cwd = ret.cwd
        ret.chroot_builddir = ret.builddir
        ret.chroot_destdir_base = ret.destdir_base
    else:
        ret.chroot_cwd = pathlib.Path("/builddir") / \
            ret.cwd.relative_to(ret.builddir)
        ret.chroot_builddir = pathlib.Path("/builddir")
        ret.chroot_destdir_base = pathlib.Path("/destdir")
        if ret.build_profile.cross:
            ret.chroot_destdir_base = ret.chroot_destdir_base / \
                ret.build_profile.triplet

    ret.chroot_destdir = ret.chroot_destdir_base \
        / f"{ret.pkgname}-{ret.pkgver}"

    ret.env["CBUILD_STATEDIR"] = "/builddir/.cbuild-" + ret.pkgname

    if not hasattr(ret, "do_install"):
        ret.error("do_install is missing")

    if not ret.force_mode and not ret._target:
        pinfo = cli.call(
            "search", ["-e", ret.pkgname],
            ret.repository, capture_output = True,
            arch = ret.build_profile.arch,
            allow_untrusted = True, use_altrepo = False
        )
        if pinfo.returncode == 0 and len(pinfo.stdout.strip()) > 0:
            foundp = pinfo.stdout.strip().decode()
            if foundp == f"{ret.pkgname}-{ret.pkgver}-r{ret.pkgrel}":
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
        sp.pkgver = ret.pkgver
        sp.pkgrel = ret.pkgrel
        sp.destdir = ret.destdir_base / f"{sp.pkgname}-{ret.pkgver}"
        sp.chroot_destdir = ret.chroot_destdir_base / f"{sp.pkgname}-{ret.pkgver}"
        sp.statedir = ret.statedir
        pinst = spf(sp)
        if not callable(pinst):
            sp.pkg_install = _subpkg_install_list(sp, pinst)
        else:
            sp.pkg_install = pinst
        # validate fields
        for fl, dval, tp, mand, asp, inh in core_fields:
            if not asp:
                continue
            flv = getattr(sp, fl)
            if tp and not isinstance(flv, tp):
                ret.error("invalid field value: %s" % fl)
        # validate build-style fields
        for fl, dval, tp, asp, inh in ret.build_style_fields:
            if not asp:
                continue
            flv = getattr(sp, fl)
            if tp and not isinstance(flv, tp):
                ret.error("invalid field value: %s" % fl)

        # deal with options
        ropts = {}

        for dopt, dtup in default_options.items():
            # only write options supported in subpackages
            if not dtup[1]:
                ropts[dopt] = ret.options[dopt]

        if sp.options:
            for opt in sp.options:
                neg = opt.startswith("!")
                if neg:
                    opt = opt[1:]
                if not opt in ropts:
                    ret.error("unknown subpackage option: %s" % opt)
                ropts[opt] = not neg

        sp.options = ropts

        # go
        ret.subpkg_list.append(sp)

    if ret.broken:
        ret.error(f"cannot be built, it's currently broken: {ret.broken}")

    if ret.cross_build and not ret.options["cross"]:
        ret.error(f"cannot be cross-compiled for {ret.cross_build}")

    if ret.bootstrapping and not ret.options["bootstrap"]:
        ret.error("attempt to bootstrap a non-bootstrap package")

    ret.statedir.mkdir(parents = True, exist_ok = True)
    ret.wrapperdir.mkdir(parents = True, exist_ok = True)

    # fill the remaining toolflag lists so it's complete
    for tf in ret.build_profile._get_supported_tool_flags():
        if not tf in ret.tool_flags:
            ret.tool_flags[tf] = []

    # when bootstrapping, use a fixed set of tools; none of the bootstrap
    # packages should be overriding these, and we want to prefer the usual
    # binutils/elftoolchain ones so we don't pull in all of llvm tools
    #
    # the llvm tools are only meaningful once we have a full chroot assembled
    # since they provide extras and possibly help in cross-compiling scenarios
    if ret.bootstrapping:
        ret.tools["CC"] = "clang"
        ret.tools["CXX"] = "clang++"
        ret.tools["CPP"] = "clang-cpp"
        ret.tools["LD"] = "ld.lld"
        ret.tools["NM"] = "nm"
        ret.tools["AR"] = "ar"
        ret.tools["AS"] = "clang"
        ret.tools["RANLIB"] = "ranlib"
        ret.tools["STRIP"] = "strip"
        # objdump explicitly not provided
        ret.tools["OBJCOPY"] = "objcopy"
        ret.tools["READELF"] = "readelf"
        ret.tools["PKG_CONFIG"] = "pkg-config"
    else:
        if not "CC" in ret.tools:
            ret.tools["CC"] = "clang"
        if not "CXX" in ret.tools:
            ret.tools["CXX"] = "clang++"
        if not "CPP" in ret.tools:
            ret.tools["CPP"] = "clang-cpp"
        if not "LD" in ret.tools:
            ret.tools["LD"] = "ld"
        if not "PKG_CONFIG" in ret.tools:
            ret.tools["PKG_CONFIG"] = "pkg-config"
        if not "NM" in ret.tools:
            ret.tools["NM"] = "llvm-nm"
        if not "AR" in ret.tools:
            ret.tools["AR"] = "llvm-ar"
        if not "AS" in ret.tools:
            ret.tools["AS"] = "clang"
        if not "RANLIB" in ret.tools:
            ret.tools["RANLIB"] = "llvm-ranlib"
        if not "STRIP" in ret.tools:
            ret.tools["STRIP"] = "llvm-strip"
        if not "OBJDUMP" in ret.tools:
            ret.tools["OBJDUMP"] = "llvm-objdump"
        if not "OBJCOPY" in ret.tools:
            ret.tools["OBJCOPY"] = "llvm-objcopy"
        if not "READELF" in ret.tools:
            ret.tools["READELF"] = "llvm-readelf"

    return ret

_tmpl_dict = {}

def read_pkg(
    pkgname, pkgarch, force_mode, run_check, jobs, build_dbg, use_ccache,
    origin, resolve = None, ignore_missing = False, target = None
):
    global _tmpl_dict

    if not isinstance(pkgname, str):
        logger.get().out_red("Missing package name.")
        raise PackageError()

    if resolve:
        for r in resolve.source_repositories:
            if (paths.distdir() / r / pkgname / "template.py").is_file():
                pkgname = f"{r}/{pkgname}"
                break
        else:
            if ignore_missing:
                return None
            logger.get().out_red("Missing template for '%s'" % pkgname)
            raise PackageError()
    elif not (paths.distdir() / pkgname / "template.py").is_file():
        if ignore_missing:
            return None
        logger.get().out_red("Missing template for '%s'" % pkgname)
        raise PackageError()

    ret = Template(pkgname, origin)
    ret.template_path = paths.distdir() / pkgname
    ret.force_mode = force_mode
    ret.bootstrapping = not pkgarch
    ret.build_dbg = build_dbg
    ret.use_ccache = use_ccache
    ret.conf_jobs = jobs
    ret._target = target

    ret.setup_reproducible()

    if pkgarch:
        ret.build_profile = profile.get_profile(pkgarch)
    else:
        ret.build_profile = profile.get_profile("bootstrap")

    if ret.build_profile.cross:
        ret.cross_build = pkgarch
    else:
        ret.cross_build = None

    ret.run_check = run_check and not ret.cross_build

    chroot.set_target(ret.build_profile.arch)

    def subpkg_deco(spkgname, cond = True):
        def deco(f):
            if cond:
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
        modh = importlib.import_module(pkgname.replace("/", ".") + ".template")

    _tmpl_dict[pkgname] = modh

    delattr(builtins, "current")
    delattr(builtins, "subpackage")

    return from_module(modh, ret)

def register_hooks():
    for step in [
        "fetch", "extract", "patch", "configure",
        "build", "check", "install", "pkg"
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
                hooks[stepn].sort(key = lambda v: v[1])
