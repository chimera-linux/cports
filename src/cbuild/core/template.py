# This file provides an interface for a parsed template that is sanitized
# (unlike a raw template, which is just plain python code).
#
# It also provides a reference to what is allowed and what is not.

import fnmatch
import shutil
import time
import glob
import pty
import sys
import os
import re
import termios
import importlib
import importlib.util
import pathlib
import contextlib
import subprocess
import builtins
import stat

from cbuild.core import logger, chroot, paths, profile, spdx, errors
from cbuild.util import compiler, flock
from cbuild.apk import cli


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


def unredir_log(pkg, fpid, oldout, olderr):
    # restore
    os.dup2(oldout, sys.stdout.fileno())
    os.dup2(olderr, sys.stderr.fileno())
    pkg.logger.fileno = sys.stdout.fileno()
    # close the old duplicates
    os.close(oldout)
    os.close(olderr)
    # wait for the logger process to finish
    os.waitpid(fpid, 0)


def sync_winsize(fd, is_pty):
    if not is_pty:
        return
    try:
        if os.isatty(sys.stdout.fileno()):
            termios.tcsetwinsize(fd, termios.tcgetwinsize(sys.stdout))
    except AttributeError:
        # not supported by this version of python
        pass


def redir_log(pkg):
    # save old descriptors
    oldout = os.dup(sys.stdout.fileno())
    olderr = os.dup(sys.stderr.fileno())
    pkg.logger.fileno = oldout
    # child will do the logging for us through a pipe or pty
    prd, prw = None, None
    colors = logger.get().use_colors
    is_pty = False
    try:
        # use a pipe if colors are suppressed, no need for pty
        if colors:
            prd, prw = pty.openpty()
            os.set_inheritable(prd, True)
            os.set_inheritable(prw, True)
            is_pty = True
    except Exception:
        pass
    if not prd:
        prd, prw = os.pipe()
    # read end propagates into child through the fork
    try:
        fpid = os.fork()
    except Exception:
        os.close(prd)
        os.close(prw)
        unredir_log(pkg, fpid, oldout, olderr)
        raise
    # set initial window size
    sync_winsize(prd, is_pty)
    # child
    if fpid == 0:
        os.close(prw)
        try:
            rarr = [bytearray(8192)]
            while True:
                # do this on each loop as the terminal may resize
                sync_winsize(prd, is_pty)
                rlen = os.readv(prd, rarr)
                if rlen == 0:
                    break
                os.write(1, rarr[0][0:rlen])
        finally:
            # raw exit (no exception) since we forked
            # don't want to propagate back to the outside
            #
            # when this triggers in case of failure, the
            # original streams should get restored in the
            # unredir_log function, so we'll lose file logs
            # but retain actual console output (hopefully)
            os._exit(0)
            return
    try:
        # in parent, close read end, we don't need it here
        os.close(prd)
        # everything goes into the pipe/pty
        os.dup2(prw, sys.stdout.fileno())
        os.dup2(prw, sys.stderr.fileno())
        # close original write end too now that it's dup
        os.close(prw)
    except Exception:
        unredir_log(pkg, fpid, oldout, olderr)
        raise
    # fire
    return fpid, oldout, olderr


# relocate "src" from root "root" to root "dest"
#
# e.g. _submove("foo/bar", "/a", "/b") will move "/b/foo/bar" to "/a/foo/bar"
#
def _submove(src, dest, root):
    src = pathlib.Path(src)
    dirs = src.parent
    ddirs = dest / dirs

    ddirs.mkdir(parents=True, exist_ok=True)

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
    "init_prepare": [],
    "pre_prepare": [],
    "do_prepare": [],
    "post_prepare": [],
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
    "post_pkg": [],
}


def run_pkg_func(pkg, func, funcn=None, desc=None, on_subpkg=False):
    if not funcn:
        if not hasattr(pkg, func):
            return False
        funcn = func
        func = getattr(pkg, funcn)
    if not desc:
        desc = funcn
    pkg.log(f"running {desc}...")
    fpid, oldout, olderr = redir_log(pkg)
    try:
        if on_subpkg:
            func()
        else:
            func(pkg)
    finally:
        unredir_log(pkg, fpid, oldout, olderr)
    return True


def call_pkg_hooks(pkg, stepn):
    for f in hooks[stepn]:
        run_pkg_func(pkg, f[0], f"{stepn}_{f[1]}", f"{stepn} hook: {f[1]}")


def _pglob_path(oldp, patp):
    if patp.is_absolute():
        rootp = pathlib.Path("/")
        return list(rootp.glob(str(patp.relative_to(rootp))))
    return list(oldp.glob(str(patp)))


def _subst_path(pkg, pathn):
    if isinstance(pathn, str) and pathn.startswith(">/"):
        return pkg.destdir / pathn.removeprefix(">/")
    else:
        return pathlib.Path(pathn)


class Package:
    def __init__(self):
        self.logger = logger.get()
        self.pkgname = None
        self.pkgver = None
        self.alternative = None

    def log(self, msg, end="\n"):
        self.logger.out(self._get_pv() + ": " + msg, end)

    def log_red(self, msg, end="\n"):
        self.logger.out_red(self._get_pv() + ": " + msg, end)

    def log_green(self, msg, end="\n"):
        self.logger.out_green(self._get_pv() + ": " + msg, end)

    def log_warn(self, msg, end="\n"):
        self.logger.warn(self._get_pv() + ": " + msg, end)

    def error(self, msg, end="\n", bt=False):
        quiet = False
        if not msg:
            msg = ""
            quiet = True
        raise errors.PackageException(msg, end, self, bt, quiet)

    def _get_pv(self):
        if self.pkgname and self.pkgver:
            return f"{self.pkgname}-{self.pkgver}-r{self.pkgrel}"
        elif self.pkgname:
            return self.pkgname
        return "cbuild"

    @contextlib.contextmanager
    def pushd(self, dirn, glob=False):
        old_path = self.rparent.cwd
        old_cpath = self.rparent.chroot_cwd

        if glob:
            new_paths = _pglob_path(old_path, _subst_path(self, dirn))
            if len(new_paths) != 1:
                self.error(
                    f"path '{dirn}' must match exactly one directory", bt=True
                )
            new_path = new_paths[0]
        else:
            new_path = old_path / _subst_path(self, dirn)

        if not new_path.is_dir():
            self.error(f"path '{new_path}' is not a directory", bt=True)

        new_path = new_path.resolve()

        self.rparent.cwd = new_path
        self.rparent.chroot_cwd = pathlib.Path("/") / new_path.relative_to(
            paths.builddir()
        )

        try:
            yield
        finally:
            self.rparent.cwd = old_path
            self.rparent.chroot_cwd = old_cpath

    def cp(self, srcp, destp, recursive=False, symlinks=True, glob=False):
        srcp = _subst_path(self, srcp)
        destp = _subst_path(self, destp)

        if not glob:
            srcs = [self.rparent.cwd / srcp]
        else:
            srcs = _pglob_path(self.rparent.cwd, srcp)
            if len(srcs) < 1:
                self.error(f"path '{srcp}' does not match any files", bt=True)

        destp = self.rparent.cwd / destp

        for srcp in srcs:
            if recursive and srcp.is_dir():
                if destp.is_dir():
                    destp = destp / srcp.name
                if srcp.is_symlink():
                    ret = shutil.copy2(srcp, destp, follow_symlinks=False)
                else:
                    ret = shutil.copytree(
                        srcp, destp, symlinks=symlinks, dirs_exist_ok=True
                    )
            elif srcp.is_dir():
                self.error(
                    f"'{srcp}' is a directory, but not using 'recursive'",
                    bt=True,
                )
            else:
                ret = shutil.copy2(srcp, destp, follow_symlinks=symlinks)

        return pathlib.Path(ret)

    def mv(self, srcp, destp, glob=False):
        srcp = _subst_path(self, srcp)
        destp = self.rparent.cwd / _subst_path(self, destp)
        if not glob:
            return pathlib.Path(shutil.move(self.rparent.cwd / srcp, destp))

        srcs = _pglob_path(self.rparent.cwd, srcp)
        if len(srcs) < 1:
            self.error(f"path '{srcp}' does not match any files", bt=True)

        ret = []
        for srcp in srcs:
            ret.append(pathlib.Path(shutil.move(srcp, destp)))

        return ret

    def mkdir(self, path, parents=False):
        (self.rparent.cwd / _subst_path(self, path)).mkdir(
            parents=parents, exist_ok=parents
        )

    def rm(self, path, recursive=False, force=False, glob=False):
        path = _subst_path(self, path)

        if not glob:
            paths = [self.rparent.cwd / path]
        else:
            paths = _pglob_path(self.rparent.cwd, path)
            if len(paths) < 1:
                self.error(f"path '{path}' does not match any files", bt=True)

        for path in paths:
            if not recursive:
                if path.is_dir() and not path.is_symlink():
                    self.error(f"'{path}' is a directory", bt=True)
                path.unlink(missing_ok=force)
            else:

                def _remove_ro(f, p, _):
                    os.chmod(p, stat.S_IWRITE)
                    f(p)

                if force and not path.exists():
                    do_unl = path.is_symlink()
                    if not do_unl:
                        return
                else:
                    do_unl = not path.is_dir() or path.is_symlink()

                if do_unl:
                    path.unlink(missing_ok=force)
                else:
                    shutil.rmtree(path, onerror=_remove_ro)

    def ln_s(self, srcp, destp, relative=False):
        srcp = _subst_path(self, srcp)
        destp = _subst_path(self, destp)
        if destp.is_dir():
            destp = destp / pathlib.Path(srcp).name
        if relative:
            srcp = os.path.relpath(srcp, start=destp.parent)
        destp.symlink_to(srcp)

    def chmod(self, path, mode):
        (self.rparent.cwd / _subst_path(self, path)).chmod(mode)

    def touch_epoch(self, path):
        ts = self.rparent.source_date_epoch
        if not ts:
            return
        self.log(f"normalizing timestamp for {path}...")
        os.utime(
            self.rparent.cwd / _subst_path(self, path),
            (ts, ts),
            follow_symlinks=False,
        )

    def find(self, path, pattern, files=False):
        path = _subst_path(self, path)
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
    "installroot": (True, True),
    "keepempty": (False, False),
    "keeplibtool": (False, False),
    "brokenlinks": (False, False),
    "hardlinks": (False, False),
    "autosplit": (True, False),
    "lintstatic": (True, False),
    "distlicense": (True, False),
    "empty": (False, False),
    # actually true by default for -devel
    "splitstatic": (False, False),
    "splitudev": (True, False),
    "splitdinit": (True, False),
    "splitdoc": (True, False),
    "scantrigdeps": (True, False),
    "scanrundeps": (True, False),
    "scanshlibs": (True, False),
    "scanpkgconf": (True, False),
    "scandevelif": (True, False),
    "scancmd": (True, False),
    "textrels": (False, False),
    "execstack": (False, False),
    "foreignelf": (False, False),
    "parallel": (True, True),
    "debug": (True, True),
    "strip": (True, False),
    "check": (True, True),
    "cross": (True, True),
    "lint": (True, True),
    "spdx": (True, False),
    "relr": (True, True),
    "lto": (True, True),
    "ltofull": (False, True),
    "ltostrip": (False, False),
    "linkparallel": (True, True),
    "linkundefver": (False, False),
    "framepointer": (True, True),
}

core_fields = [
    # name default type mandatory subpkg inherit
    # core fields that are set early
    ("license", None, str, True, True, True),
    ("pkgdesc", None, str, True, True, True),
    ("pkgname", None, str, True, False, False),
    ("pkgrel", None, int, True, False, False),
    ("pkgver", None, str, True, False, False),
    ("url", None, str, True, False, False),
    ("maintainer", None, str, True, False, False),
    # various options that can be set for the template
    ("options", [], list, False, True, False),
    # other core-ish fields
    ("broken", None, str, False, False, False),
    ("restricted", None, str, False, False, False),
    ("build_style", None, str, False, False, False),
    # sources
    ("sha256", [], (list, str), False, False, False),
    ("source", [], (list, str), False, False, False),
    ("source_paths", None, list, False, False, False),
    # target support
    ("archs", None, list, False, False, False),
    # build directory and patches
    ("build_wrksrc", "", str, False, False, False),
    ("patch_args", [], list, False, False, False),
    ("prepare_after_patch", False, bool, False, False, False),
    # dependency lists
    ("checkdepends", [], list, False, False, False),
    ("hostmakedepends", [], list, False, False, False),
    ("makedepends", [], list, False, False, False),
    ("depends", [], list, False, True, False),
    # other package lists + related
    ("provides", [], list, False, True, False),
    ("provider_priority", 0, int, False, True, True),
    ("replaces", [], list, False, True, False),
    ("replaces_priority", 0, int, False, True, True),
    ("install_if", [], list, False, True, False),
    ("ignore_shlibs", [], list, False, True, False),
    # build systems
    ("configure_args", [], list, False, False, False),
    ("configure_script", "configure", str, False, False, False),
    ("configure_env", {}, dict, False, False, False),
    ("configure_gen", [], list, False, False, False),
    ("make_cmd", "bmake", str, False, False, False),
    ("make_dir", ".", str, False, False, False),
    ("make_env", {}, dict, False, False, False),
    ("make_wrapper", [], list, False, False, False),
    ("make_build_args", [], list, False, False, False),
    ("make_install_args", [], list, False, False, False),
    ("make_check_args", [], list, False, False, False),
    ("make_build_target", "", str, False, False, False),
    ("make_install_target", "install", str, False, False, False),
    ("make_check_target", "check", str, False, False, False),
    ("make_build_env", {}, dict, False, False, False),
    ("make_install_env", {}, dict, False, False, False),
    ("make_check_env", {}, dict, False, False, False),
    ("make_build_wrapper", [], list, False, False, False),
    ("make_install_wrapper", [], list, False, False, False),
    ("make_check_wrapper", [], list, False, False, False),
    # target build related
    ("protected_paths", [], list, False, True, False),
    ("nostrip_files", [], list, False, True, False),
    ("hardening", [], list, False, True, False),
    ("nopie_files", [], list, False, True, False),
    ("tools", {}, dict, False, False, False),
    ("tool_flags", {}, dict, False, False, False),
    ("env", {}, dict, False, False, False),
    ("debug_level", -1, int, False, False, False),
    # packaging
    ("origin", None, str, False, True, True),
    ("triggers", [], list, False, True, False),
    ("scriptlets", {}, dict, False, True, False),
    ("file_modes", {}, dict, False, True, False),
    ("file_xattrs", {}, dict, False, True, False),
    ("broken_symlinks", [], list, False, True, False),
    ("compression", None, "comp", False, True, True),
    # wrappers
    ("exec_wrappers", [], list, False, False, False),
    # scriptlet generators
    ("system_users", [], list, False, True, False),
    ("system_groups", [], list, False, True, False),
    # fields relating to build fields
    # cmake
    ("cmake_dir", None, str, False, False, False),
    # makefile
    ("make_use_env", False, bool, False, False, False),
    # meson
    ("meson_dir", ".", str, False, False, False),
    # golang
    ("go_mod_dl", None, str, False, False, False),
    ("go_build_tags", [], list, False, False, False),
    ("go_check_tags", [], list, False, False, False),
]

# a field priority list, the second element indicates whether
# the field should have a higher priority than its preceeding
# field (i.e. False means it has the same priority)
core_fields_priority = [
    ("pkgname", True),
    ("pkgver", True),
    ("pkgrel", True),
    ("archs", True),
    ("build_wrksrc", True),
    ("build_style", True),
    ("prepare_after_patch", True),
    ("configure_script", True),
    ("configure_args", True),
    ("configure_env", True),
    ("configure_gen", True),
    ("make_cmd", True),
    ("make_dir", True),
    ("make_env", True),
    ("make_wrapper", True),
    ("make_build_target", True),
    ("make_build_args", True),
    ("make_build_env", True),
    ("make_build_wrapper", True),
    ("make_install_target", True),
    ("make_install_args", True),
    ("make_install_env", True),
    ("make_install_wrapper", True),
    ("make_check_target", True),
    ("make_check_args", True),
    ("make_check_env", True),
    ("make_check_wrapper", True),
    ("make_use_env", True),
    ("cmake_dir", False),
    ("meson_dir", False),
    ("hostmakedepends", True),
    ("makedepends", True),
    ("checkdepends", True),
    ("depends", False),
    ("go_mod_dl", True),
    ("go_build_tags", False),
    ("go_check_tags", False),
    ("provides", True),
    ("provider_priority", True),
    ("replaces", True),
    ("replaces_priority", True),
    ("install_if", True),
    ("ignore_shlibs", True),
    ("triggers", True),
    ("scriptlets", True),
    ("origin", True),
    ("pkgdesc", True),
    ("maintainer", True),
    ("license", True),
    ("url", True),
    ("source", True),
    ("source_paths", True),
    ("sha256", True),
    ("debug_level", True),
    ("patch_args", True),
    ("tools", True),
    ("tool_flags", True),
    ("env", True),
    ("protected_paths", True),
    ("nostrip_files", True),
    ("nopie_files", True),
    ("file_modes", True),
    ("file_xattrs", True),
    ("broken_symlinks", True),
    ("compression", True),
    ("hardening", True),
    ("options", True),
    ("exec_wrappers", True),
    ("system_users", True),
    ("system_groups", True),
    ("restricted", True),
    ("broken", True),
]

# this will map field names to numerical indexes
core_fields_map = None

cross_tools = {
    "CC": True,
    "CXX": True,
    "CPP": True,
    "LD": True,
    "PKG_CONFIG": True,
}

sites = {
    "sourceforge": "https://downloads.sourceforge.net/sourceforge",
    "freedesktop": "https://freedesktop.org/software",
    "mozilla": "https://ftp.mozilla.org/pub",
    "debian": "http://ftp.debian.org/debian/pool",
    "ubuntu": "http://archive.ubuntu.com/ubuntu/pool",
    "nongnu": "https://download.savannah.nongnu.org/releases",
    "kernel": "https://www.kernel.org/pub/linux",
    "gnome": "https://download.gnome.org/sources",
    "xorg": "https://www.x.org/releases/individual",
    "cpan": "https://www.cpan.org/modules/by-module",
    "pypi": "https://files.pythonhosted.org/packages/source",
    "gnu": "https://ftp.gnu.org/gnu",
    "kde": "https://download.kde.org/stable",
    "xfce": "https://archive.xfce.org/src",
}


# for defaults, always make copies
def copy_of_dval(val):
    if isinstance(val, list):
        return list(val)
    if isinstance(val, dict):
        return dict(val)
    return val


def validate_type(val, tp):
    if not tp:
        return True
    if tp == "comp":
        if val is None:
            return True
        sv = val.split(":")
        if len(sv) < 0 or len(sv) > 2:
            return False
        match sv[0]:
            case "deflate" | "zstd":
                if len(sv) == 2:
                    try:
                        iv = int(sv[1])
                        if iv < 0 or iv > (9 if sv[0] == "deflate" else 22):
                            return False
                    except Exception:
                        return False
            case "none":
                return len(sv) == 1
            case _:
                return False
        return True
    if isinstance(tp, tuple):
        for rt in tp:
            if isinstance(val, rt):
                break
        else:
            return False
    elif not isinstance(val, tp):
        return False
    return True


def pkg_profile(pkg, target):
    if pkg.stage == 0 and (target == "host" or target == "target"):
        return profile.get_profile("bootstrap")
    elif target == "host":
        return profile.get_profile(chroot.host_cpu())
    elif target == "target":
        return pkg._target_profile
    elif target == "target:native":
        return pkg._target_profile._native_profile
    elif not target:
        return pkg._current_profile

    return profile.get_profile(target)


class Template(Package):
    def __init__(self, pkgname, origin):
        super().__init__()

        if origin:
            self.origin_pkg = origin
        else:
            self.origin_pkg = self

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
            except Exception:
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
        self.subpackages = []
        self.all_subpackages = []
        self.subpkg_list = []
        self.source_date_epoch = None
        self.git_revision = None
        self.git_dirty = False
        self.current_sonames = {}
        self._license_install = False

    def get_build_deps(self):
        from cbuild.core import dependencies

        def _resolve_bdep(opkg, depn):
            for sr in opkg.source_repositories:
                rp = paths.distdir() / sr
                tp = rp / depn / "template.py"
                if tp.is_file():
                    pn = tp.resolve().parent.name
                    return sr, pn
            return None, None

        bdeps = {}
        visited = {}
        hds, tds, rds = dependencies.setup_depends(self, True)
        for bd in hds + tds:
            if bd in visited:
                continue
            visited[bd] = True
            sr, pn = _resolve_bdep(self, bd)
            # just ignore unresolved stuff here, it's ok for now
            if sr:
                bdeps[f"{sr}/{pn}"] = True
        for orig, bd in rds:
            if bd in visited:
                continue
            visited[bd] = True
            sr, pn = _resolve_bdep(self, bd)
            # we need to ignore subpackages depending on their neighbors
            if sr and ((bd == orig) or (pn != self.pkgname)):
                bdeps[f"{sr}/{pn}"] = True
        # pre-sort it just in case
        return sorted(bdeps.keys())

    def dump(self):
        metadata = {}
        mlist = []
        subpkgs = []

        dumped = {
            "pkgname": self.pkgname,
            "pkgver": self.pkgver,
            "pkgrel": self.pkgrel,
            "pkgdesc": self.pkgdesc,
            "license": self.license,
            "maintainer": self.maintainer,
            "url": self.url,
            "broken": self.broken,
            "restricted": self.restricted,
            "subpackages": subpkgs,
            "variables": metadata,
        }

        for sp in self.subpkg_list:
            subpkg = {
                "pkgname": sp.pkgname,
            }
            slist = []
            for fl, dval, tp, mand, asp, inh in core_fields:
                if fl in subpkg or not asp:
                    continue
                slist.append((fl, getattr(sp, fl)))
            # append
            slist.sort(key=lambda v: v[0])
            for k, v in slist:
                subpkg[k] = v
            subpkgs.append(sp.pkgname)

        for fl, dval, tp, mand, sp, inh in core_fields:
            # skip stuff in the primary dump
            if fl in dumped:
                continue
            mlist.append((fl, getattr(self, fl)))

        mlist.sort(key=lambda v: v[0])

        for k, v in mlist:
            metadata[k] = v

        return dumped

    def setup_reproducible(self):
        if self.source_date_epoch:
            return

        self.source_date_epoch = int(time.time())

        if not shutil.which("git"):
            # no git, not reproducible
            return

        if (
            subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                capture_output=True,
                cwd=self.template_path,
            ).returncode
            != 0
        ):
            # not in a git repository
            return

        # find whether the template dir has local modifications
        dirty = (
            len(
                subprocess.run(
                    ["git", "status", "-s", "--", self.template_path],
                    capture_output=True,
                ).stdout.strip()
            )
            != 0
        )

        def _gitlog(fmt, tgt, pkg):
            bargs = ["git", "log", "-n1", f"--format={fmt}"]
            if pkg:
                bargs += ["--", tgt]
            else:
                bargs.append(tgt)
            return (
                subprocess.run(bargs, capture_output=True)
                .stdout.strip()
                .decode("ascii")
            )

        # find the last revision modifying the template
        grev = _gitlog("%H", self.template_path, True)

        # 0 length means untracked in git
        if len(grev) != 40 and len(grev) != 0:
            self.error(f"invalid commit format for {self.template_path}")

        self.git_revision = grev
        self.git_dirty = dirty

        # template directory modified or not tracked, no  reproducible date
        if dirty or not grev:
            return

        # get the date of the git revision
        ts = _gitlog("%ct", grev, False)

        try:
            self.source_date_epoch = int(ts)
        except ValueError:
            self.error(f"invalid commit timestamp for {self.template_path}")

    def build_lint(self):
        if self.broken:
            self.error(self.broken)

        if self.stage == 0 and not self.options["bootstrap"]:
            self.error("attempt to bootstrap a non-bootstrap package")

        if not hasattr(self, "do_install"):
            self.error("do_install is missing")

        # ensure subpackages have correct style and symlinks
        repo = self.repository
        bpn = self.pkgname
        for sp in self.subpkg_list:
            if sp.build_style and sp.build_style != self.build_style:
                self.error("subpackages cannot change build-style")

            tlink = f"{repo}/{sp.pkgname}"
            tpath = paths.distdir() / tlink
            if not tpath.is_symlink():
                self.error(f"subpackage '{sp.pkgname}' is missing a symlink")
            if str(tpath.readlink()) != bpn:
                self.error(f"subpackage '{sp.pkgname}' has incorrect symlink")

        if not cli.check_version(f"{self.pkgver}-r{self.pkgrel}"):
            self.error("pkgver has an invalid format")

        # validate other stuff
        self.validate_pkgdesc()
        self.validate_maintainer()
        self.validate_url()
        self.validate_order()
        self.validate_spdx()

    def ensure_fields(self):
        for fl, dval, tp, mand, sp, inh in core_fields:
            # mandatory fields are all at the beginning
            if not mand:
                break
            # basic validation of type
            if not hasattr(self, fl) or not validate_type(
                getattr(self, fl), tp
            ):
                self.error("missing or invalid field: %s" % fl)

    def validate_spdx(self):
        # validate license if we need to
        if self.options["spdx"]:
            lerr = None
            try:
                self._license_install = spdx.validate(self.license)
            except RuntimeError as e:
                lerr = str(e)
            if lerr:
                self.error("failed validating license: %s" % lerr)

            for sp in self.subpkg_list:
                if sp.license == self.license:
                    continue

                lerr = None
                try:
                    sp._license_install = spdx.validate(sp.license)
                except RuntimeError as e:
                    lerr = str(e)
                if lerr:
                    self.error(
                        "failed validating subpackage license: %s" % lerr
                    )

    def validate_url(self):
        # do not validate if not linting
        if not self.options["lint"]:
            return

        from urllib.parse import urlparse

        succ = True

        try:
            uval = urlparse(self.url)
        except Exception:
            succ = False

        if not succ:
            self.error("failed to parse url")

        if (uval.scheme != "http") and (uval.scheme != "https"):
            self.error("url must be http or https")

        if uval.path.endswith("/"):
            self.error("url path must not end with a slash")

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

    def validate_maintainer(self):
        # do not validate if not linting
        if not self.options["lint"]:
            return

        m = re.fullmatch(r"^(.+) <([^>]+)>$", self.maintainer)
        if not m:
            self.error("maintainer has an invalid format")

        grp = m.groups()

        if grp[0] != " ".join(grp[0].split()):
            self.error("maintainer name has an invalid format")

        addrp = r"^[A-Za-z0-9._%+=-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$"

        if not re.fullmatch(addrp, grp[1]):
            self.error("maintainer email has an invalid format")

    def validate_order(self):
        global core_fields_map
        # do not validate if not linting
        if not self.options["lint"]:
            return
        # otherwise we need a mapping of var names to indexes
        if not core_fields_map:
            core_fields_map = {}
            # initialize the priority mapping if not done already
            idx = 0
            for n, pinc in core_fields_priority:
                if pinc:
                    idx += 1
                core_fields_map[n] = idx
        # by default assume success
        succ = True
        precomment = False
        # we must read and parse the file
        with open(self.template_path / "template.py") as f:
            midx = 0
            midx_line = None
            msg = None
            for ln in f:
                # an empty line aborts the lint
                if ln == "\n":
                    break
                sln = ln.strip()
                # non-empty or commented line skips the line
                if len(sln) == 0:
                    continue
                if sln.startswith("#"):
                    precomment = True
                    continue
                # a non-assignment skips the line
                ass = ln.find("=")
                if ass < 0:
                    continue
                # get the assigned name
                vnm = ln[0:ass].strip()
                # not an actual name or it starts with underscore, so skip it
                if not vnm.isidentifier() or vnm.startswith("_"):
                    continue
                # if options has check disabled, a reason must be given
                if vnm == "options":
                    if not self.options["check"] and not precomment:
                        self.error(
                            "lint failed: check disabled but no reason given"
                        )
                # reset comment presence
                precomment = False
                # unknown variables must go last, so they get a fallback index
                cidx = core_fields_map.get(vnm, len(core_fields_priority))
                if cidx < midx:
                    msg = f"'{midx_line}' should go after '{vnm}'"
                elif cidx > midx:
                    midx = cidx
                    midx_line = vnm
                    if msg:
                        succ = False
                        self.log_red(msg)
                        msg = None
            # we have reached the end, print the message if any
            if msg:
                succ = False
                self.log_red(msg)
        # if failed, error out
        if not succ:
            self.error("lint failed: incorrect variable order")
        # validate vars
        for varn in vars(self._raw_mod):
            # custom vars should be underscored
            if varn.startswith("_"):
                continue
            # if it's a known hook/var, skip
            if callable(getattr(self._raw_mod, varn)):
                # skip if it's a function and in hooks
                if varn in hooks:
                    continue
                else:
                    self.log_red(f"unknown hook: {varn}")
                    succ = False
            else:
                # skip if it's non-function and in fields
                if varn in core_fields_map:
                    continue
                else:
                    self.log_red(f"unknown variable: {varn}")
                    succ = False
        # error if anything failed
        if not succ:
            self.error("lint failed: invalid vars/hooks in template")

    def validate_arch(self):
        # if already broken, skip validating it
        if self.broken:
            return
        bprof = self.profile()
        archn = bprof.arch
        # no archs specified: we match always
        if not self.archs:
            return
        # bad archs type
        if not isinstance(self.archs, list):
            self.broken = "archs field is malformed, cannot build"
            return
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
                    self.broken = (
                        f"conflicting arch patterns: {v}, !{v}, cannot build"
                    )
                    return
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
                self.broken = (
                    f"ambiguous arch patterns: {prevmatch}, {v}, cannot build"
                )
                return
            # otherwise consider the one with longer exact match
            if nexactcur > nexactprev:
                prevmatch = v
                prevneg = curneg
        # no match or negative match
        if not prevmatch or prevneg:
            self.broken = f"this package cannot be built for {archn}"
        # otherwise we're good

    def is_built(self, quiet=False):
        archn = self.profile().arch
        with flock.lock(flock.apklock(archn)):
            pinfo = cli.call(
                "search",
                ["--from", "none", "-e", self.pkgname],
                self.repository,
                capture_output=True,
                arch=archn,
                allow_untrusted=True,
                allow_network=False,
                use_altrepo=False,
            )
            if pinfo.returncode == 0 and len(pinfo.stdout.strip()) > 0:
                foundp = pinfo.stdout.strip().decode()
                if foundp == f"{self.pkgname}-{self.pkgver}-r{self.pkgrel}":
                    if self.origin_pkg == self and not quiet:
                        # TODO: print the repo somehow
                        self.log(f"found ({pinfo.stdout.strip().decode()})")
                    return True
            return False

    def do(
        self,
        cmd,
        *args,
        env=None,
        wrksrc=None,
        capture_output=False,
        stdout=None,
        stderr=None,
        input=None,
        check=True,
        allow_network=False,
        path=None,
    ):
        cpf = self.profile()

        cenv = {
            "CBUILD_TARGET_MACHINE": cpf.arch,
            "CBUILD_TARGET_SYSROOT": str(cpf.sysroot),
            "CBUILD_HOST_MACHINE": chroot.host_cpu(),
        }

        fakestrip = self.wrapperdir / "strip"
        if self.stage > 0:
            fakestrip = self.chroot_statedir / fakestrip.relative_to(
                self.statedir
            )

        cenv["STRIPBIN"] = str(fakestrip)

        # cflags and so on
        for k in self.tool_flags:
            cenv[k] = self.get_tool_flags(k, shell=True)

        if self.source_date_epoch:
            cenv["SOURCE_DATE_EPOCH"] = str(self.source_date_epoch)
        if cpf.triplet:
            cenv["CBUILD_TARGET_TRIPLET"] = cpf.triplet

        if self.use_ccache:
            cenv["CCACHEPATH"] = "/usr/lib/ccache/bin"
            cenv["CCACHE_DIR"] = "/cbuild_cache/ccache"
            cenv["CCACHE_COMPILERCHECK"] = "content"
            cenv["CCACHE_COMPRESS"] = "1"
            cenv["CCACHE_BASEDIR"] = str(self.chroot_cwd)

        if (
            self.use_sccache
            and (self.bldroot_path / "usr/bin/sccache").exists()
        ):
            cenv["RUSTC_WRAPPER"] = "/usr/bin/sccache"
            cenv["SCCACHE_DIR"] = "/cbuild_cache/sccache"
            cenv["SCCACHE_IDLE_TIMEOUT"] = "30"

        cenv.update(self.tools)

        cenv["CC"] = self.get_tool("CC")
        cenv["CXX"] = self.get_tool("CXX")
        cenv["CPP"] = self.get_tool("CPP")
        cenv["LD"] = self.get_tool("LD")
        cenv["PKG_CONFIG"] = self.get_tool("PKG_CONFIG")

        with self.profile("host") as hpf:
            for k in ["CC", "CXX", "CPP", "LD", "PKG_CONFIG"]:
                cenv[f"BUILD_{k}"] = cenv[f"{k}_FOR_BUILD"] = self.get_tool(k)

            # cflags and so on
            for k in self.tool_flags:
                cenv[f"BUILD_{k}"] = cenv[f"{k}_FOR_BUILD"] = (
                    self.get_tool_flags(k, shell=True)
                )

            if hpf.triplet:
                cenv["CBUILD_HOST_TRIPLET"] = hpf.triplet

        cenv.update(self.env)
        if env:
            cenv.update(env)

        wdir = self.chroot_cwd
        if wrksrc:
            wdir = wdir / wrksrc

        fakeroot = False
        if self.current_phase == "install" and self.options["installroot"]:
            fakeroot = True
        elif self.current_phase == "check" and self.options["checkroot"]:
            fakeroot = True

        # to avoid host fakeroot dependency
        if self.stage == 0:
            fakeroot = False

        if self.current_phase == "fetch":
            allow_network = True
        elif (
            self.current_phase != "extract"
            and self.current_phase != "patch"
            and self.current_phase != "prepare"
        ):
            allow_network = False

        lld_args = compiler._get_lld_cpuargs(self.link_threads)
        if self.options["linkundefver"]:
            lld_args += ["--undefined-version"]
        if self.use_ltocache:
            lld_args += [
                f"--thinlto-cache-policy=cache_size_bytes={self.use_ltocache}",
                "--thinlto-cache-dir=/cbuild_cache/lld_thinlto_cache",
            ]

        return chroot.enter(
            cmd,
            *args,
            capture_output=capture_output,
            env=cenv,
            wrkdir=wdir,
            check=check,
            bootstrapping=self.stage == 0,
            ro_root=True,
            ro_build=self.install_done,
            ro_dest=(self.current_phase != "install"),
            mount_cbuild_cache=True,
            unshare_all=not allow_network,
            fakeroot=fakeroot,
            stdout=stdout,
            stderr=stderr,
            input=input,
            lldargs=lld_args,
            binpath=path,
            term=True,
        )

    def stamp(self, name):
        return StampCheck(self, name)

    def run_step(self, stepn, optional=False, skip_post=False):
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
        self, name, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return pkg_profile(self, target)._get_tool_flags(
            self, name, extra_flags, hardening, shell
        )

    def get_cflags(
        self, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return self.get_tool_flags(
            "CFLAGS", extra_flags, hardening, shell, target
        )

    def get_cxxflags(
        self, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return self.get_tool_flags(
            "CXXFLAGS", extra_flags, hardening, shell, target
        )

    def get_fflags(
        self, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return self.get_tool_flags(
            "FFLAGS", extra_flags, hardening, shell, target
        )

    def get_ldflags(
        self, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return self.get_tool_flags(
            "LDFLAGS", extra_flags, hardening, shell, target
        )

    def get_rustflags(
        self, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return self.get_tool_flags(
            "RUSTFLAGS", extra_flags, hardening, shell, target
        )

    def get_goflags(
        self, extra_flags=[], hardening=[], shell=False, target=None
    ):
        return self.get_tool_flags(
            "GOFLAGS", extra_flags, hardening, shell, target
        )

    def get_tool(self, name, target=None):
        if name not in self.tools:
            return None

        target = pkg_profile(self, target)

        if name in cross_tools and target.cross:
            # special case for cross toolchains
            if not self.pkgname.endswith("-cross"):
                return f"{target.triplet}-{self.tools[name]}"

        return self.tools[name]

    def has_hardening(self, hname, target=None):
        target = pkg_profile(self, target)

        return profile.get_hardening(target, self)[hname]

    def has_lto(self, target=None):
        target = pkg_profile(self, target)

        return self.options["lto"] and target._has_lto(self.stage)

    @contextlib.contextmanager
    def _profile(self, target):
        old_tgt = self._current_profile

        if self.stage == 0 and (target == "host" or target == "target"):
            target = "bootstrap"
        elif target == "host":
            target = chroot.host_cpu()
        elif target == "target":
            target = self._target_profile.arch
        elif target == "target:native":
            target = f"{self._target_profile.arch}:native"

        try:
            self._current_profile = profile.get_profile(target)
            yield self._current_profile
        finally:
            self._current_profile = old_tgt

    def profile(self, target=None):
        if target is None:
            return self._current_profile
        return self._profile(target)

    def uninstall(self, path, glob=False):
        if path.startswith("/"):
            raise errors.TracebackException(
                f"uninstall: path '{path}' must not be absolute"
            )
        if not glob:
            dests = [self.destdir / path]
            if not dests[0].exists() and not dests[0].is_symlink():
                self.error(f"path '{path}' does not match anything", bt=True)
        else:
            dests = list(self.destdir.glob(path))
            if len(dests) < 1:
                self.error(f"path '{path}' does not match anything", bt=True)
        for dst in dests:
            self.rm(dst, recursive=True, force=True)

    def rename(self, src, dest, relative=True, glob=False, keep_name=False):
        if src.startswith("/"):
            raise errors.TracebackException(
                f"uninstall: path '{src}' must not be absolute"
            )
        if dest.startswith("/"):
            raise errors.TracebackException(
                f"uninstall: path '{dest}' must not be absolute"
            )
        if glob:
            tsrc = list(self.destdir.glob(src))
            if len(tsrc) != 1:
                self.error(f"rename glob '{src}' must match one result")
            src = tsrc[0]
        else:
            src = self.destdir / src
        if relative:
            dest = (src.resolve(True).parent / dest).resolve()
        else:
            dest = (self.destdir / dest).resolve()
        if keep_name:
            dest.mkdir(parents=True, exist_ok=True)
            src.rename(dest / src.name)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dest)

    def install_files(self, path, dest, symlinks=True, name=None):
        path = _subst_path(self, path)
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            raise errors.TracebackException(
                f"install_files: path '{dest}' must not be absolute"
            )

        path = self.cwd / path
        dfn = self.destdir / dest / (name or path.name)

        if path.is_dir():
            shutil.copytree(path, dfn, symlinks=symlinks)
        else:
            self.install_dir(dest)
            shutil.copy2(path, dfn)

    def install_dir(self, dest, mode=0o755, empty=False):
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            raise errors.TracebackException(
                f"install_dir: path '{dest}' must not be absolute"
            )
        dirp = self.destdir / dest
        if not dirp.is_dir():
            dirp.mkdir(parents=True)
        if mode is not None:
            dirp.chmod(mode)
        if empty:
            (dirp / ".empty").touch(mode=0o644)

    def install_file(self, src, dest, mode=0o644, name=None, glob=False):
        if not glob:
            srcs = [self.cwd / pathlib.Path(src)]
        else:
            if name:
                self.error("cannot specify 'name' and 'glob' together", bt=True)
            srcs = list(self.cwd.glob(src))
            if len(srcs) < 1:
                self.error(f"path '{src}' does not match any files", bt=True)
        dest = pathlib.Path(dest)
        # sanitize destination
        if dest.is_absolute():
            raise errors.TracebackException(
                f"install_file: path '{dest}' must not be absolute"
            )
        for src in srcs:
            # copy
            if name:
                dfn = self.destdir / dest / name
            else:
                dfn = self.destdir / dest / src.name
            if dfn.exists():
                raise errors.TracebackException(
                    f"install_file: destination file '{dfn}' already exists"
                )
            self.install_dir(dest)
            shutil.copy2(self.cwd / src, dfn)
            if mode is not None:
                dfn.chmod(mode)

    def install_bin(self, src, mode=0o755, name=None, glob=False):
        self.install_file(src, "usr/bin", mode, name, glob)

    def install_lib(self, src, mode=0o755, name=None, glob=False):
        self.install_file(src, "usr/lib", mode, name, glob)

    def install_man(self, src, name=None, cat=None, glob=False):
        self.install_dir("usr/share/man")
        manbase = self.destdir / "usr/share/man"
        if not glob:
            srcs = [self.cwd / src]
        else:
            if name:
                self.error("cannot specify 'name' and 'glob' together", bt=True)
            srcs = list(self.cwd.glob(src))
            if len(srcs) < 1:
                self.error(f"path '{src}' does not match any files", bt=True)
        for absmn in srcs:
            mnf = absmn.name
            if not cat:
                if len(absmn.suffix) == 0:
                    raise errors.TracebackException(
                        f"install_man: manpage '{mnf}' has no section"
                    )
                try:
                    mcat = int(absmn.suffix[1:])
                except Exception:
                    raise errors.TracebackException(
                        f"install_man: manpage '{mnf}' has an invalid section"
                    )
            else:
                mcat = cat
            mandir = manbase / f"man{mcat}"
            mandir.mkdir(parents=True, exist_ok=True)
            if name:
                mnf = f"{name}.{mcat}"
            shutil.copy2(absmn, mandir / mnf)
            (mandir / mnf).chmod(0o644)

    def install_license(self, src, name=None, pkgname=None):
        self.install_file(
            src, "usr/share/licenses/" + (pkgname or self.pkgname), 0o644, name
        )

    def install_completion(self, src, shell, name=None):
        if not name:
            name = self.pkgname
        match shell:
            case "bash":
                self.install_file(
                    src, "usr/share/bash-completion/completions", name=name
                )
            case "zsh":
                self.install_file(
                    src, "usr/share/zsh/site-functions", name=f"_{name}"
                )
            case "fish":
                self.install_file(
                    src,
                    "usr/share/fish/vendor_completions.d",
                    name=f"{name}.fish",
                )
            case _:
                self.error(f"unknown shell: {shell}")

    def install_service(self, src, name=None, enable=False):
        src = pathlib.Path(src)
        if src.suffix == ".user":
            svname = name or src.with_suffix("").name
            self.install_file(src, "etc/dinit.d/user", name=svname)
            if enable:
                self.install_dir("usr/lib/dinit.d/user/boot.d")
                self.install_link(
                    f"usr/lib/dinit.d/user/boot.d/{svname}", f"../{svname}"
                )
        else:
            svname = name or src.name
            self.install_file(src, "etc/dinit.d", name=svname)
            if enable:
                self.install_dir("usr/lib/dinit.d/boot.d")
                self.install_link(
                    f"usr/lib/dinit.d/boot.d/{svname}", f"../{svname}"
                )

    def install_svscript(self, src, name=None):
        self.install_file(src, "etc/dinit.d/scripts", mode=0o755, name=name)

    def install_tmpfiles(self, src, name=None):
        svname = name or self.pkgname
        self.install_file(src, "usr/lib/tmpfiles.d", name=f"{svname}.conf")

    def install_sysusers(self, src, name=None):
        svname = name or self.pkgname
        self.install_file(src, "usr/lib/sysusers.d", name=f"{svname}.conf")

    def install_link(self, dest, tgt, absolute=False):
        dest = pathlib.Path(dest)
        if dest.is_absolute():
            raise errors.TracebackException(
                f"install_link: path '{dest}' must not be absolute"
            )
        dest = self.destdir / dest
        if not absolute and str(tgt).startswith("/"):
            raise errors.TracebackException(
                f"install_link: target '{tgt}' must not be absolute"
            )
        dest.symlink_to(tgt)

    def install_shell(self, *args):
        self.install_dir("etc/shells.d")
        for s in args:
            self.install_link(
                f"etc/shells.d/{os.path.basename(s)}", s, absolute=True
            )


def _default_take_extra(self, extra):
    if extra is not None:
        if isinstance(extra, list):
            for v in extra:
                self.take(v)
        else:
            extra()


def _split_static(pkg):
    for f in (pkg.parent.destdir / "usr/lib").rglob("*.a"):
        pkg.take(str(f.relative_to(pkg.parent.destdir)))


def _split_pycache(pkg):
    pyver = getattr(pkg.parent.rparent, "python_version", None)
    if not pyver:
        return

    pyver = pyver.replace(".", "")

    for f in pkg.parent.destdir.rglob("__pycache__"):
        if not f.is_dir():
            continue
        for ff in f.glob(f"*.cpython-{pyver}.*pyc"):
            pkg.take(str(ff.relative_to(pkg.parent.destdir)))
        for ff in f.glob("*.py[co]"):
            pkg.error(f"illegal pycache: {ff.name}")


def _split_dlinks(pkg):
    pkg.take("usr/lib/dinit.d/boot.d", missing_ok=True)
    pkg.take("usr/lib/dinit.d/user/boot.d", missing_ok=True)


def _split_fishcomp(pkg):
    pkg.take("usr/share/fish/completions", missing_ok=True)
    pkg.take("usr/share/fish/vendor_completions.d", missing_ok=True)


def _split_locale(pkg):
    pkg.take("usr/share/locale", missing_ok=True)
    # lxqt uses its own special dir since it uses a .qm format
    pkg.take("usr/share/lxqt/translations", missing_ok=True)


autopkgs = [
    # dbg is handled by its own hook
    ("dbg", "debug files", None, None),
    # static is kinda special
    ("static", "static libraries", "base-devel-static", _split_static),
    ("doc", "documentation", "base-doc", lambda p: p.take_doc()),
    (
        "man",
        "manual pages",
        "base-man",
        lambda p: p.take("usr/share/man", missing_ok=True),
    ),
    (
        "dinit",
        "service files",
        "dinit-chimera",
        lambda p: p.take("etc/dinit.d", missing_ok=True),
    ),
    # foo-dinit-links installs if foo-dinit installs
    ("dinit-links", "service links", "-dinit", _split_dlinks),
    (
        "initramfs-tools",
        "initramfs scripts",
        "initramfs-tools",
        lambda p: p.take("usr/share/initramfs-tools", missing_ok=True),
    ),
    (
        "udev",
        "udev rules",
        "base-udev",
        lambda p: p.take("usr/lib/udev", missing_ok=True),
    ),
    (
        "bashcomp",
        "bash completions",
        "bash-completion",
        lambda p: p.take("usr/share/bash-completion", missing_ok=True),
    ),
    (
        "zshcomp",
        "zsh completions",
        "zsh",
        lambda p: p.take("usr/share/zsh/site-functions", missing_ok=True),
    ),
    (
        "fishcomp",
        "fish completions",
        "fish-shell",
        _split_fishcomp,
    ),
    (
        "locale",
        "locale data",
        "base-locale",
        _split_locale,
    ),
    ("pycache", "Python bytecode", "python-pycache", _split_pycache),
]


class Subpackage(Package):
    def __init__(self, name, parent, oldesc=None, alternative=None):
        super().__init__()

        self.pkgname = name
        self.parent = parent
        self.rparent = parent

        self.pkgver = parent.pkgver
        self.pkgrel = parent.pkgrel
        self.statedir = parent.statedir
        self.build_style = parent.build_style
        self.alternative = alternative

        self.destdir = (
            parent.rparent.destdir_base / f"{self.pkgname}-{self.pkgver}"
        )
        self.chroot_destdir = (
            parent.rparent.chroot_destdir_base / f"{self.pkgname}-{self.pkgver}"
        )

        # default subpackage fields
        for fl, dval, tp, mand, sp, inh in core_fields:
            if not sp:
                continue
            if inh:
                setattr(self, fl, copy_of_dval(getattr(parent.rparent, fl)))
            else:
                setattr(self, fl, copy_of_dval(dval))

        ddeps = []
        bdep = None
        instif = None

        if not oldesc:
            # strip the old suffix for non-automatic subpackages, if any
            oldesc = re.sub(r" \(.+\)$", "", self.pkgdesc)

        # default suffixes
        if name.endswith("-devel"):
            self.pkgdesc = oldesc + " (development files)"
        elif name.endswith("-libs"):
            self.pkgdesc = oldesc + " (libraries)"
        elif name.endswith("-progs"):
            self.pkgdesc = oldesc + " (programs)"
        else:
            for apkg, adesc, iif, takef in autopkgs:
                sfx = f"-{apkg}"
                if name.endswith(sfx) and name != f"base{sfx}":
                    bdep = name.removesuffix(sfx)
                    if iif and iif.startswith("-"):
                        bdep += iif
                        instif = name
                    else:
                        instif = iif
                    self.pkgdesc = oldesc + f" ({adesc})"

        # by default some subpackages depend on their parent package
        if bdep:
            fbdep = f"{bdep}={parent.pkgver}-r{parent.pkgrel}"
            if not name.endswith("-man") and not name.endswith("-doc"):
                ddeps.append(fbdep)
            # they may also get automatically installed
            if instif:
                if instif == name:
                    self.install_if = [fbdep]
                else:
                    if instif == "python-pycache":
                        # this applies for auto-subpkgs at the relevant
                        # stage, as those are created using the parent
                        # very late; for any manually declared stuff
                        # this is fixed up in pre_pkg/005_py_dep
                        pyver = getattr(parent.rparent, "python_version", None)
                        if pyver:
                            instif = f"{instif}~{pyver}"
                            # we want pycaches to soft-pull the right python,
                            # in order for them to affect staging (leave no
                            # outdated pycache behind)
                            ddeps.append(f"base-python{pyver}~{pyver}")
                    elif not instif.startswith("base-"):
                        ddeps.append(instif)
                    self.install_if = [fbdep, instif]

        self.depends = ddeps

        self.force_mode = parent.rparent.force_mode
        self.stage = parent.rparent.stage
        self._license_install = False

    def take(self, p, missing_ok=False):
        p = pathlib.Path(p)
        if p.is_absolute():
            self.error(f"take(): path '{p}' must not be absolute")
        origp = self.parent.destdir / p
        got = glob.glob(str(origp))
        if len(got) == 0 and not missing_ok:
            self.error(f"take(): path '{p}' did not match anything")
        for fullp in got:
            # relative path to the file/dir in original destdir
            pdest = self.parent.destdir
            self.log(f"moving: {fullp} -> {self.destdir}")
            _submove(
                pathlib.Path(fullp).relative_to(pdest), self.destdir, pdest
            )

    def make_link(self, path, tgt):
        dstp = self.destdir / path
        self.log(f"symlink: {dstp} -> {tgt}")
        self.mkdir(dstp.parent, parents=True)
        self.ln_s(tgt, dstp)

    def take_static(self):
        self.take("usr/lib/*.a")

    def take_devel(self, man="23"):
        for f in (self.parent.destdir / "usr/bin").glob("*-config"):
            if f.name != "pkg-config":
                self.take(f"usr/bin/{f.name}")
        self.take("usr/lib/*.a", missing_ok=True)
        # .so files are a bit special
        # we have no mechanism for bypassing errors for the special case,
        # but it's always wrong to devel actual ELF files, so the warning
        # is just in case (for linker scripts, it breaks dep tracer, but
        # can we do anything about that?)
        for f in (self.parent.destdir / "usr/lib").glob("*.so"):
            if f.is_symlink():
                self.take(f"usr/lib/{f.name}")
                continue
            # check if ELF
            with open(f, "rb") as sof:
                if sof.read(4) == b"\x7fELF":
                    self.log_warn(
                        f"{f}: unsuffixed ELF .so encountered, skipping for devel"
                    )
                    continue
            # otherwise maybe a linker script? take it
            self.log_warn(
                f"{f}: unsuffixed non-ELF .so encountered, linker script? (check dependencies)"
            )
            self.take(f"usr/lib/{f.name}")
        self.take("usr/lib/pkgconfig", missing_ok=True)
        self.take("usr/lib/cmake", missing_ok=True)
        self.take("usr/lib/glade/modules", missing_ok=True)
        self.take("usr/include", missing_ok=True)
        self.take("usr/share/cmake", missing_ok=True)
        self.take("usr/share/pkgconfig", missing_ok=True)
        self.take("usr/share/aclocal", missing_ok=True)
        self.take("usr/share/gettext", missing_ok=True)
        self.take("usr/share/vala/vapi", missing_ok=True)
        self.take("usr/share/gir-[0-9]*", missing_ok=True)
        self.take("usr/share/glade/catalogs", missing_ok=True)
        if man:
            mpath = self.parent.destdir / "usr/share/man/man1"
            for f in mpath.glob("*-config.1"):
                if f.stem != "pkg-config":
                    self.take(f"usr/share/man/man1/{f.name}")
            self.take(f"usr/share/man/man[{man}]", missing_ok=True)

    def take_doc(self):
        self.take("usr/share/doc", missing_ok=True)
        self.take("usr/share/info", missing_ok=True)
        self.take("usr/share/html", missing_ok=True)
        self.take("usr/share/licenses", missing_ok=True)
        self.take("usr/share/gtk-doc", missing_ok=True)
        self.take("usr/share/ri", missing_ok=True)
        self.take("usr/share/help", missing_ok=True)
        self.take("usr/share/devhelp/books", missing_ok=True)

    def take_libs(self):
        self.take("usr/lib/lib*.so.[0-9]*")
        self.take("usr/lib/girepository-[0-9]*", missing_ok=True)

    def take_progs(self, man="18"):
        self.take("usr/bin/*")
        self.take("usr/share/bash-completion", missing_ok=True)
        self.take("usr/share/zsh", missing_ok=True)
        self.take("usr/share/fish/completions", missing_ok=True)
        self.take("usr/share/fish/vendor_completions.d", missing_ok=True)
        if man:
            self.take(f"usr/share/man/man[{man}]", missing_ok=True)

    def default_devel(self, man="23", extra=None):
        def func():
            self.take_devel(man)
            _default_take_extra(self, extra)

        return func

    def default_static(self, extra=None):
        def func():
            self.take_static()
            _default_take_extra(self, extra)

        return func

    def default_doc(self, extra=None):
        def func():
            self.take_doc()
            _default_take_extra(self, extra)

        return func

    def default_libs(self, extra=None):
        def func():
            self.take_libs()
            _default_take_extra(self, extra)

        return func

    def default_progs(self, man="18", extra=None):
        def func():
            self.take_progs(man)
            _default_take_extra(self, extra)

        return func


def _subpkg_install_list(self, lst):
    def real_install():
        for it in lst:
            if it.startswith("?"):
                self.take(it.removeprefix("?"), missing_ok=True)
            elif it.startswith("@"):
                sd = it.removeprefix("@").split("=>")
                if len(sd) != 2 or len(sd[0]) == 0 or len(sd[1]) == 0:
                    self.error(f"malformed symlink spec '{it}'")
                self.make_link(*sd)
            else:
                self.take(it)

    return real_install


def _interp_url(pkg, url):
    if not url.startswith("$("):
        return url

    import re

    def matchf(m):
        mw = m.group(1).removesuffix("_SITE").lower()
        if mw not in sites:
            pkg.error(f"malformed source URL '{url}'", bt=True)
        return sites[mw]

    return re.sub(r"\$\((\w+)\)", matchf, url)


def from_module(m, ret):
    if not m:
        return None

    prevpkg = ret.pkgname

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

    # ensure pkgname is the same
    if ret.pkgname != prevpkg:
        ret.error(f"pkgname does not match template ({prevpkg})")

    # ensure pkgname is lowercase
    if ret.pkgname.lower() != ret.pkgname:
        ret.error("package name must be lowercase")

    # ensure origin is filled
    ret.origin = ret.pkgname

    # possibly skip very early once we have the bare minimum info
    if (
        not ret.force_mode
        and not ret.bulk_mode
        and not ret.current_target
        and ret.is_built()
    ):
        raise SkipPackage()

    # fill in core non-mandatory fields
    for fl, dval, tp, mand, sp, inh in core_fields:
        # already set
        if mand:
            continue
        # also perform type validation
        if hasattr(m, fl):
            flv = getattr(m, fl)
            if not validate_type(flv, tp):
                ret.error("invalid field value: %s" % fl)
            # validated, set
            setattr(ret, fl, flv)

    # transform options
    ropts = {}

    for dopt, dtup in default_options.items():
        ropts[dopt] = dtup[0]

    if ret.pkgname.endswith("-devel"):
        ropts["splitstatic"] = True

    if ret.options:
        for opt in ret.options:
            neg = opt.startswith("!")
            if neg:
                opt = opt[1:]
            if opt not in ropts:
                ret.error("unknown option: %s" % opt)
            ropts[opt] = not neg

    ret.options = ropts

    if ret.provider_priority < 0:
        ret.error("provider_priority must be positive")
    if ret.replaces_priority < 0:
        ret.error("replaces_priority must be positive")

    # the real job count
    if not ret.options["parallel"]:
        ret.make_jobs = 1
    else:
        ret.make_jobs = ret.conf_jobs

    if not ret.options["linkparallel"]:
        ret.link_threads = 1
    else:
        ret.link_threads = ret.conf_link_threads

    ret.build_style_defaults = []

    if ret.build_style:
        importlib.import_module(f"cbuild.build_style.{ret.build_style}").use(
            ret
        )

    # perform initialization
    if hasattr(m, "init"):
        m.init(ret)

    # set default fields for build_style if not set by template
    for fl, dval in ret.build_style_defaults:
        if not hasattr(m, fl):
            setattr(ret, fl, copy_of_dval(dval))

    # add our own methods
    for phase in [
        "fetch",
        "extract",
        "prepare",
        "patch",
        "configure",
        "build",
        "check",
        "install",
    ]:
        if hasattr(m, "init_" + phase):
            setattr(ret, "init_" + phase, getattr(m, "init_" + phase))
        if hasattr(m, "pre_" + phase):
            setattr(ret, "pre_" + phase, getattr(m, "pre_" + phase))
        if hasattr(m, "do_" + phase):
            setattr(ret, "do_" + phase, getattr(m, "do_" + phase))
        if hasattr(m, "post_" + phase):
            setattr(ret, "post_" + phase, getattr(m, "post_" + phase))

    bdirbase = paths.builddir() / "builddir"
    cbdirbase = pathlib.Path("/builddir")

    # paths that can be used by template methods
    ret.files_path = ret.template_path / "files"
    ret.patches_path = ret.template_path / "patches"
    ret.sources_path = paths.sources() / f"{ret.pkgname}-{ret.pkgver}"
    ret.bldroot_path = paths.bldroot()
    ret.statedir = bdirbase / (".cbuild-" + ret.pkgname)
    ret.wrapperdir = ret.statedir / "wrappers"

    if ret.profile().cross:
        ret.destdir_base = paths.builddir() / "destdir" / ret.profile().triplet
    else:
        ret.destdir_base = paths.builddir() / "destdir"

    ret.destdir = ret.destdir_base / f"{ret.pkgname}-{ret.pkgver}"

    ret.srcdir = bdirbase / f"{ret.pkgname}-{ret.pkgver}"
    ret.cwd = ret.srcdir / ret.build_wrksrc

    if ret.stage == 0:
        ret.chroot_cwd = ret.cwd
        ret.chroot_srcdir = ret.srcdir
        ret.chroot_statedir = ret.statedir
        ret.chroot_destdir_base = ret.destdir_base
        ret.chroot_sources_path = ret.sources_path
    else:
        ret.chroot_cwd = cbdirbase / ret.cwd.relative_to(bdirbase)
        ret.chroot_srcdir = cbdirbase / ret.srcdir.relative_to(bdirbase)
        ret.chroot_statedir = cbdirbase / ret.statedir.relative_to(bdirbase)
        ret.chroot_destdir_base = pathlib.Path("/destdir")
        ret.chroot_sources_path = (
            pathlib.Path("/sources") / f"{ret.pkgname}-{ret.pkgver}"
        )
        if ret.profile().cross:
            ret.chroot_destdir_base = (
                ret.chroot_destdir_base / ret.profile().triplet
            )

    ret.chroot_destdir = ret.chroot_destdir_base / f"{ret.pkgname}-{ret.pkgver}"

    ret.env["CBUILD_STATEDIR"] = "/builddir/.cbuild-" + ret.pkgname

    spdupes = {}
    # link subpackages and fill in their fields
    for spn, spf, spa in ret.subpackages:
        if spa:
            spn = f"{spa}-{spn}-default"
        if spn in spdupes:
            ret.error(f"subpackage '{spn}' already exists")
        if spn.lower() != spn:
            ret.error(f"subpackage '{spn}' must be lowercase")
        spdupes[spn] = True
        sp = Subpackage(spn, ret, alternative=spa)
        pinst = spf(sp)
        if isinstance(pinst, list):
            sp.pkg_install = _subpkg_install_list(sp, pinst)
        elif callable(pinst):
            sp.pkg_install = pinst
        else:
            ret.error(f"invalid return for subpackage '{spn}'")
        # validate fields
        for fl, dval, tp, mand, asp, inh in core_fields:
            if not asp:
                continue
            flv = getattr(sp, fl)
            if not validate_type(flv, tp):
                ret.error("invalid field value: %s" % fl)

        # deal with options
        ropts = {}

        for dopt, dtup in default_options.items():
            if dtup[1]:
                # global opt: inherit value
                ropts[dopt] = ret.options[dopt]
            else:
                # per-package opt: set default
                ropts[dopt] = dtup[0]

        if sp.pkgname.endswith("-devel"):
            ropts["splitstatic"] = True

        if sp.options:
            for opt in sp.options:
                neg = opt.startswith("!")
                if neg:
                    opt = opt[1:]
                if opt not in ropts:
                    ret.error("unknown subpackage option: %s" % opt)
                ropts[opt] = not neg

        sp.options = ropts

        # go
        ret.subpkg_list.append(sp)

    # sometimes things need to know if a package is buildable
    if ret.broken:
        ret.broken = f"cannot be built, it's currently broken: {ret.broken}"
    elif ret.restricted and not ret._allow_restricted:
        ret.broken = f"cannot be built, it's restricted: {ret.restricted}"
    elif ret.repository not in _allow_cats:
        ret.broken = f"cannot be built, disallowed by cbuild (not in {', '.join(_allow_cats)})"
    elif ret.profile().cross and not ret.options["cross"]:
        ret.broken = f"cannot be cross-compiled for {ret.profile().arch}"

    # if archs is present, validate it, it may mark the package broken
    ret.validate_arch()

    # fill the remaining toolflag lists so it's complete
    for tf in ret.profile()._get_supported_tool_flags():
        if tf not in ret.tool_flags:
            ret.tool_flags[tf] = []

    if "CC" not in ret.tools:
        ret.tools["CC"] = "clang"
    if "CXX" not in ret.tools:
        ret.tools["CXX"] = "clang++"
    if "CPP" not in ret.tools:
        ret.tools["CPP"] = "clang-cpp"
    if "LD" not in ret.tools:
        ret.tools["LD"] = "ld.lld"
    if "PKG_CONFIG" not in ret.tools:
        ret.tools["PKG_CONFIG"] = "pkg-config"
    if "NM" not in ret.tools:
        ret.tools["NM"] = "nm"
    if "AR" not in ret.tools:
        ret.tools["AR"] = "ar"
    if "AS" not in ret.tools:
        ret.tools["AS"] = "clang"
    if "RANLIB" not in ret.tools:
        ret.tools["RANLIB"] = "ranlib"
    if "STRIP" not in ret.tools:
        ret.tools["STRIP"] = "strip"
    if "OBJDUMP" not in ret.tools:
        ret.tools["OBJDUMP"] = "objdump"
    if "OBJCOPY" not in ret.tools:
        ret.tools["OBJCOPY"] = "objcopy"
    if "READELF" not in ret.tools:
        ret.tools["READELF"] = "readelf"

    # ensure sources and checksums are a list
    if not isinstance(ret.source, list):
        ret.source = [ret.source]
    if isinstance(ret.sha256, str):
        ret.sha256 = [ret.sha256]

    # expand source
    for i in range(len(ret.source)):
        ret.source[i] = _interp_url(ret, ret.source[i])

    return ret


_tmpl_dict = {}


def read_mod(
    pkgname,
    pkgarch,
    force_mode,
    run_check,
    jobs,
    build_dbg,
    caches,
    origin,
    resolve=None,
    ignore_missing=False,
    target=None,
    force_check=False,
    autopkg=False,
    stage=3,
    bulk_mode=False,
    allow_restricted=True,
):
    global _tmpl_dict

    if not isinstance(pkgname, str):
        raise errors.CbuildException("missing package name")

    if resolve:
        resolved = False
        for r in resolve.source_repositories:
            rpath = paths.distdir() / r
            if (rpath / pkgname / "template.py").is_file():
                pkgname = f"{r}/{pkgname}"
                resolved = True
                break
        if not resolved and autopkg:
            altname = None
            for apkg, adesc, iif, takef in autopkgs:
                if pkgname.endswith(f"-{apkg}"):
                    altname = pkgname.removesuffix(f"-{apkg}")
                    break
            if altname:
                for r in resolve.source_repositories:
                    rpath = paths.distdir() / r
                    if (rpath / altname / "template.py").is_file():
                        pkgname = f"{r}/{altname}"
                        resolved = True
                        break
        if not resolved:
            if ignore_missing:
                return None, None
            raise errors.CbuildException(f"missing template for '{pkgname}'")
    else:
        # if a valid path to template.py, try translating to pkgname
        tmplp = pathlib.Path(pkgname).resolve()
        if tmplp.name == "template.py" and tmplp.is_file():
            pkgname = f"{tmplp.parent.parent.name}/{tmplp.parent.name}"
        # otherwise validate the format
        pnl = pkgname.split("/")
        if len(pnl) == 3 and pnl[2] == "":
            pnl = pnl[:-1]
        if len(pnl) != 2 and not ignore_missing:
            raise errors.CbuildException(
                f"template name '{pkgname}' has an invalid format"
            )
        pkgname = "/".join(pnl)
        if not (paths.distdir() / pkgname / "template.py").is_file():
            if ignore_missing:
                return None, None
            raise errors.CbuildException(f"missing template for '{pkgname}'")

    tmplp = (paths.distdir() / pkgname).resolve()
    pkgname = str(tmplp.relative_to(paths.distdir()))

    ret = Template(pkgname, origin)
    ret.template_path = tmplp
    ret.force_mode = force_mode
    ret.bulk_mode = bulk_mode
    ret.build_dbg = build_dbg
    ret.use_ccache = caches[0] if caches else None
    ret.use_sccache = caches[1] if caches else None
    ret.use_ltocache = caches[2] if caches else None
    ret.conf_jobs = jobs[0]
    ret.conf_link_threads = jobs[1]
    ret.stage = stage
    ret._custom_targets = {}
    ret.current_target = target
    ret._force_check = force_check
    ret._allow_restricted = allow_restricted

    if pkgarch:
        ret._current_profile = profile.get_profile(pkgarch)
    else:
        ret._current_profile = profile.get_profile("bootstrap")

    ret.run_check = run_check and not ret._current_profile.cross

    ret._target_profile = ret._current_profile

    def subpkg_deco(spkgname, cond=True, alternative=None):
        def deco(f):
            if alternative:
                pn = f"{alternative}-{spkgname}-default"
            else:
                pn = spkgname
            ret.all_subpackages.append(pn)
            if cond:
                ret.subpackages.append((spkgname, f, alternative))

        return deco

    def target_deco(tname, tdep):
        def deco(f):
            ret._custom_targets[tname] = (f, tdep)

        return deco

    setattr(builtins, "subpackage", subpkg_deco)
    setattr(builtins, "custom_target", target_deco)
    setattr(builtins, "self", ret)

    modh, modspec = _tmpl_dict.get(pkgname, (None, None))
    if modh:
        # found in cache, gonna need to clear the module handle
        # and then reexec it to populate it with fresh contents
        for fld in dir(modh):
            # don't mess with the internals
            if fld.startswith("__") and fld.endswith("__"):
                continue
            delattr(modh, fld)
    else:
        # never loaded, build a fresh spec and handle
        modspec = importlib.util.spec_from_file_location(
            pkgname, paths.distdir() / pkgname / "template.py"
        )
        modh = importlib.util.module_from_spec(modspec)
        # cache
        _tmpl_dict[pkgname] = (modh, modspec)

    modspec.loader.exec_module(modh)

    delattr(builtins, "self")
    delattr(builtins, "subpackage")

    ret._raw_mod = modh

    return modh, ret


def read_pkg(
    pkgname,
    pkgarch,
    force_mode,
    run_check,
    jobs,
    build_dbg,
    caches,
    origin,
    resolve=None,
    ignore_missing=False,
    target=None,
    force_check=False,
    autopkg=False,
    stage=3,
    bulk_mode=False,
    allow_restricted=True,
):
    modh, ret = read_mod(
        pkgname,
        pkgarch,
        force_mode,
        run_check,
        jobs,
        build_dbg,
        caches,
        origin,
        resolve,
        ignore_missing,
        target,
        force_check,
        autopkg,
        stage,
        bulk_mode,
        allow_restricted,
    )
    return from_module(modh, ret)


def register_cats(cats):
    global _allow_cats
    _allow_cats = cats


def get_cats():
    return _allow_cats


def register_hooks():
    for step in [
        "fetch",
        "extract",
        "prepare",
        "patch",
        "configure",
        "build",
        "check",
        "install",
        "pkg",
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
                hooks[stepn].sort(key=lambda v: v[1])
