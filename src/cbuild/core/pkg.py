import os
import shutil
import stat


pkg_stack = []
pkg_failed = None


def push(pkg):
    pkg_stack.append(pkg)


def pop():
    return pkg_stack.pop()


def failed():
    global pkg_failed
    retv = pkg_failed
    pkg_failed = None
    return retv


def set_failed(pkg):
    global pkg_failed
    if not pkg_failed:
        pkg_failed = pkg


def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)


def remove_pkg_wrksrc(pkg):
    if pkg.srcdir.is_dir():
        pkg.log("cleaning build directory...")
        shutil.rmtree(pkg.srcdir, onerror=_remove_ro)


def remove_pkg_statedir(pkg):
    if pkg.statedir.is_dir():
        shutil.rmtree(pkg.statedir, onerror=_remove_ro)


def remove_pkg(pkg):
    if not pkg.destdir.is_dir():
        return

    p = pkg.profile()
    crossb = p.arch if p.cross else ""

    def remove_state(spkg, dbase):
        (pkg.statedir / f"{spkg.pkgname}_{crossb}_subpkg_install_done").unlink(
            missing_ok=True
        )
        (pkg.statedir / f"{spkg.pkgname}_{crossb}_prepkg_done").unlink(
            missing_ok=True
        )

    pkg.log("cleaning destination directory...")

    remove_state(pkg, pkg.destdir_base)
    for sp in pkg.subpkg_list:
        remove_state(sp, pkg.destdir_base)

    shutil.rmtree(pkg.destdir_base, onerror=_remove_ro)

    (pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done").unlink(
        missing_ok=True
    )
    (pkg.statedir / f"{pkg.pkgname}_{crossb}_pre_install_done").unlink(
        missing_ok=True
    )
    (pkg.statedir / f"{pkg.pkgname}_{crossb}_post_install_done").unlink(
        missing_ok=True
    )
