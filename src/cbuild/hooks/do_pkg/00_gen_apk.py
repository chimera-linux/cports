from cbuild.core import logger, paths
from cbuild.apk import create as apk_c, sign as apk_s

import glob
import time
import pathlib
import subprocess

def genpkg(
    pkg, repo, arch, binpkg, destdir = None, dbg = False
):
    if not destdir:
        destdir = pkg.destdir

    if not destdir.is_dir():
        pkg.log_warn(f"cannot find pkg destdir, skipping...")
        return

    binpath = repo / binpkg
    lockpath = binpath.with_suffix(binpath.suffix + ".lock")

    repo.mkdir(parents = True, exist_ok = True)

    while lockpath.is_file():
        pkg.log_warn(f"binary package being created, waiting...")
        time.sleep(1)

    try:
        lockpath.touch()

        metadata = {}
        args = []

        pkgdesc = pkg.pkgdesc
        if dbg:
            pkgdesc += " (debug files)"

        metadata["pkgdesc"] = pkgdesc
        metadata["url"] = pkg.rparent.url
        metadata["maintainer"] = pkg.rparent.maintainer
        #metadata["packager"] = pkg.rparent.maintainer
        metadata["origin"] = pkg.rparent.pkgname
        metadata["license"] = pkg.license

        if pkg.rparent.git_revision:
            metadata["commit"] = pkg.rparent.git_revision + (
                "-dirty" if pkg.rparent.git_dirty else ""
            )

        if not dbg and len(pkg.provides) > 0:
            pkg.provides.sort()
            metadata["provides"] = pkg.provides

        if pkg.provider_priority > 0:
            metadata["provider_priority"] = pkg.provider_priority

        mdeps = []

        if not dbg:
            for c in pkg.depends:
                mdeps.append(c)
        else:
            mdeps.append(f"{pkg.pkgname}={pkg.pkgver}-r{pkg.pkgrel}")

        mdeps.sort()
        metadata["depends"] = mdeps

        metadata["install_if"] = list(pkg.install_if)

        if not dbg:
            if hasattr(pkg, "aso_provides"):
                pkg.aso_provides.sort(key = lambda x: x[0])
                metadata["shlib_provides"] = pkg.aso_provides

            if hasattr(pkg, "so_requires"):
                pkg.so_requires.sort()
                metadata["shlib_requires"] = pkg.so_requires

            if hasattr(pkg, "pc_provides"):
                pkg.pc_provides.sort()
                metadata["pc_provides"] = pkg.pc_provides

            if hasattr(pkg, "cmd_provides"):
                pkg.cmd_provides.sort()
                metadata["cmd_provides"] = pkg.cmd_provides

            if hasattr(pkg, "pc_requires"):
                pkg.pc_requires.sort()
                metadata["pc_requires"] = pkg.pc_requires

            if len(pkg.triggers) > 0:
                # check validity first
                for t in pkg.triggers:
                    p = pathlib.Path(t)
                    if not p or not p.is_absolute():
                        pkg.error(f"invalid trigger path: {t}")
                # finally pass metadata
                metadata["triggers"] = list(pkg.triggers)

            metadata["file_modes"] = pkg.file_modes

        logger.get().out(f"Creating {binpkg} in repository {repo}...")

        pkgname = pkg.pkgname
        if dbg:
            pkgname += "-dbg"

        apk_c.create(
            pkgname, f"{pkg.pkgver}-r{pkg.pkgrel}", arch,
            pkg.rparent.source_date_epoch, destdir, pkg.statedir, binpath,
            pkg.rparent.signing_key, metadata
        )
    finally:
        lockpath.unlink()

def invoke(pkg):
    arch = pkg.rparent.profile().arch
    binpkg = f"{pkg.pkgname}-{pkg.pkgver}-r{pkg.pkgrel}.apk"
    binpkg_dbg = f"{pkg.pkgname}-dbg-{pkg.pkgver}-r{pkg.pkgrel}.apk"

    repo = paths.repository() / pkg.rparent.repository

    if pkg.pkgname.endswith("-dbg"):
        repo = repo / "debug"

    repo = repo / ".stage" / arch

    genpkg(pkg, repo, arch, binpkg)

    for sp in pkg.rparent.subpkg_list:
        if sp.pkgname == f"{pkg.rparent.pkgname}-dbg":
            # if there's an explicit subpkg for -dbg, don't autogenerate
            return

    dbgdest = pkg.rparent.destdir_base / f"{pkg.pkgname}-dbg-{pkg.pkgver}"

    # don't have a dbg destdir
    if not dbgdest.is_dir():
        return

    repo = paths.repository() / pkg.rparent.repository / "debug/.stage" / arch

    genpkg(pkg, repo, arch, binpkg_dbg, dbgdest, True)
