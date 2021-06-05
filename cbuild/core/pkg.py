from cbuild.core import logger, chroot, xbps
from os import path
import os
import shutil

def remove_autodeps(pkg):
    pkg.log(f"removing autodeps...")

    x = chroot.invoke_reconfigure(["-a"], capture_out = True)
    sout = x.stdout
    serr = x.stderr

    x = chroot.invoke_xcmd(
        xbps.remove(), ["-Ryod"], capture_out = True, yes_input = True
    )
    while x.returncode == 0:
        if len(x.stdout.strip()) == 0:
            break
        sout += x.stdout
        serr += x.stderr
        x = chroot.invoke_xcmd(
            xbps.remove(), ["-Ryod"], capture_out = True,
            yes_input = True
        )

    if x.returncode != 0:
        sout = sout.strip()
        serr = serr.strip()
        if len(sout) > 0:
            pkg.logger.out_plain(">> stdout:")
            pkg.logger.out_plain(sout.decode("ascii"))
        if len(serr) > 0:
            pkg.logger.out_plain(">> stderr:")
            pkg.logger.out_plain(serr.decode("ascii"))
        pkg.error(f"failed to remove autodeps ({x.returncode})")

def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)

def remove_pkg_wrksrc(pkg):
    if path.isdir(pkg.abs_wrksrc):
        pkg.log("cleaning build directory...")
        shutil.rmtree(pkg.abs_wrksrc, onerror = _remove_ro)

def remove_pkg_statedir(pkg):
    if path.isdir(pkg.statedir):
        shutil.rmtree(pkg.statedir, onerror = _remove_ro)

def remove_pkg(pkg):
    if not path.isdir(pkg.destdir):
        return

    def remove_spkg(spkg, dbase):
        tpath = dbase / f"{spkg.pkgname}-{pkg.version}"
        if path.isdir(tpath):
            spkg.log(f"removing files from destdir...")
            shutil.rmtree(tpath, onerror = _remove_ro)
        tpath = dbase / f"{spkg.pkgname}-dbg-{pkg.version}"
        if path.isdir(tpath):
            spkg.log(f"removing dbg files from destdir...")
            shutil.rmtree(tpath, onerror = _remove_ro)
        try:
            os.remove(pkg.statedir / f"{spkg.pkgname}__subpkg_install_done")
        except FileNotFoundError:
            pass
        try:
            os.remove(pkg.statedir / f"{spkg.pkgname}__prepkg_done")
        except FileNotFoundError:
            pass

    remove_spkg(pkg, pkg.destdir_base)
    for sp in pkg.subpkg_list:
        remove_spkg(sp, pkg.destdir_base)

    try:
        os.remove(pkg.statedir / f"{pkg.pkgname}__install_done")
    except FileNotFoundError:
        pass
    try:
        os.remove(pkg.statedir / f"{pkg.pkgname}__pre_install_done")
    except FileNotFoundError:
        pass
    try:
        os.remove(pkg.statedir / f"{pkg.pkgname}__post_install_done")
    except FileNotFoundError:
        pass
