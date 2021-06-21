from cbuild.core import logger, paths, chroot
import os
import shutil
import subprocess

def remove_autodeps(pkg):
    pkg.log(f"removing autodeps...")

    failed = False

    if subprocess.run([
        "apk", "info", "--root", str(paths.masterdir()), "autodeps-host"
    ], capture_output = True).returncode == 0:
        del_ret = chroot.enter("apk", [
            "del", "autodeps-host"
        ], capture_out = True)
        if del_ret.returncode != 0:
            pkg.logger.out_plain(">> stderr (host):")
            pkg.logger.out_plain(del_ret.stderr.decode())
            failed = True

    if subprocess.run([
        "apk", "info", "--root", str(paths.masterdir()), "autodeps-target"
    ], capture_output = True).returncode == 0:
        del_ret = chroot.enter("apk", [
            "del", "autodeps-target"
        ], capture_out = True)
        if del_ret.returncode != 0:
            pkg.logger.out_plain(">> stderr (target):")
            pkg.logger.out_plain(del_ret.stderr.decode())
            failed = True

    if failed:
        pkg.error("failed to remove autodeps")

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
