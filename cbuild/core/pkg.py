from cbuild.core import logger, xbps
import os
import shutil

def remove_autodeps(pkg):
    pkg.log(f"removing autodeps...")

    success, sout, serr = xbps.reconfigure(capture_out = True)

    if success:
        success, sout, serr = xbps.remove_orphans()

    if not success:
        sout = sout.strip()
        serr = serr.strip()
        if len(sout) > 0:
            pkg.logger.out_plain(">> stdout:")
            pkg.logger.out_plain(sout.decode("ascii"))
        if len(serr) > 0:
            pkg.logger.out_plain(">> stderr:")
            pkg.logger.out_plain(serr.decode("ascii"))
        pkg.error(f"failed to remove autodeps")

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

    def remove_spkg(spkg, dbase):
        tpath = dbase / f"{spkg.pkgname}-{pkg.version}"
        if tpath.is_dir():
            spkg.log(f"removing files from destdir...")
            shutil.rmtree(tpath, onerror = _remove_ro)
        tpath = dbase / f"{spkg.pkgname}-dbg-{pkg.version}"
        if tpath.is_dir():
            spkg.log(f"removing dbg files from destdir...")
            shutil.rmtree(tpath, onerror = _remove_ro)
        (pkg.statedir / f"{spkg.pkgname}__subpkg_install_done").unlink(
            missing_ok = True
        )
        (pkg.statedir / f"{spkg.pkgname}__prepkg_done").unlink(missing_ok = True)

    remove_spkg(pkg, pkg.destdir_base)
    for sp in pkg.subpkg_list:
        remove_spkg(sp, pkg.destdir_base)

    (pkg.statedir / f"{pkg.pkgname}__install_done").unlink(missing_ok = True)
    (pkg.statedir / f"{pkg.pkgname}__pre_install_done").unlink(
        missing_ok = True
    )
    (pkg.statedir / f"{pkg.pkgname}__post_install_done").unlink(
        missing_ok = True
    )
