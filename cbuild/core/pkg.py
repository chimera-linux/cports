from cbuild.core import logger, paths, chroot
import os
import shutil
import subprocess

def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)

def remove_pkg_wrksrc(pkg):
    if pkg.abs_wrksrc.is_dir():
        pkg.log("cleaning build directory...")
        shutil.rmtree(pkg.abs_wrksrc, onerror = _remove_ro)

def remove_pkg_statedir(pkg):
    if pkg.statedir.is_dir():
        shutil.rmtree(pkg.statedir, onerror = _remove_ro)

def remove_pkg(pkg):
    if not pkg.destdir.is_dir():
        return

    crossb = pkg.cross_build if pkg.cross_build else ""

    def remove_spkg(spkg, dbase):
        tpath = dbase / f"{spkg.pkgname}-{pkg.version}"
        if tpath.is_dir():
            spkg.log(f"removing files from destdir...")
            shutil.rmtree(tpath, onerror = _remove_ro)
        tpath = dbase / f"{spkg.pkgname}-dbg-{pkg.version}"
        if tpath.is_dir():
            spkg.log(f"removing dbg files from destdir...")
            shutil.rmtree(tpath, onerror = _remove_ro)
        (pkg.statedir / f"{spkg.pkgname}_{crossb}_subpkg_install_done").unlink(
            missing_ok = True
        )
        (pkg.statedir / f"{spkg.pkgname}_{crossb}_prepkg_done").unlink(
            missing_ok = True
        )

    remove_spkg(pkg, pkg.destdir_base)
    for sp in pkg.subpkg_list:
        remove_spkg(sp, pkg.destdir_base)

    (pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done").unlink(
        missing_ok = True
    )
    (pkg.statedir / f"{pkg.pkgname}_{crossb}_pre_install_done").unlink(
        missing_ok = True
    )
    (pkg.statedir / f"{pkg.pkgname}_{crossb}_post_install_done").unlink(
        missing_ok = True
    )
