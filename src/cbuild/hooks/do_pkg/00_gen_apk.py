from cbuild.core import logger, paths
from cbuild.apk import create as apk_c, sign as apk_s

import glob
import time
import pathlib
import subprocess

_hooks = [
    "pre-install", "post-install",
    "pre-upgrade", "post-upgrade",
    "pre-deinstall", "post-deinstall"
]

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
        metadata["license"] = pkg.rparent.license

        if pkg.rparent.git_revision:
            metadata["commit"] = pkg.rparent.git_revision + (
                "-dirty" if pkg.rparent.git_dirty else ""
            )

        if not dbg and len(pkg.provides) > 0:
            metadata["provides"] = pkg.provides

        mdeps = []

        if not dbg:
            for c in pkg.depends:
                mdeps.append(c)
        else:
            mdeps.append(f"{pkg.pkgname}={pkg.pkgver}-r{pkg.pkgrel}")

        metadata["depends"] = mdeps

        if not dbg:
            if hasattr(pkg, "aso_provides"):
                metadata["shlib_provides"] = pkg.aso_provides

            if hasattr(pkg, "so_requires"):
                metadata["shlib_requires"] = pkg.so_requires

            mhooks = []
            for h in _hooks:
                hf = pkg.rparent.template_path / (pkg.pkgname + "." + h)
                if hf.is_file():
                    mhooks.append(hf)

            if len(mhooks) > 0:
                metadata["hooks"] = mhooks

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
    arch = pkg.rparent.build_profile.arch
    binpkg = f"{pkg.pkgname}-{pkg.pkgver}-r{pkg.pkgrel}.apk"
    binpkg_dbg = f"{pkg.pkgname}-dbg-{pkg.pkgver}-r{pkg.pkgrel}.apk"

    repo = paths.repository() / pkg.rparent.repository / arch

    genpkg(pkg, repo, arch, binpkg)

    for sp in pkg.rparent.subpkg_list:
        if sp.pkgname == f"{pkg.rparent.pkgname}-dbg":
            # if there's an explicit subpkg for -dbg, don't autogenerate
            return

    dbgdest = pkg.rparent.destdir_base / f"{pkg.pkgname}-dbg-{pkg.pkgver}"

    # don't have a dbg destdir
    if not dbgdest.is_dir():
        return

    repo = paths.repository() / pkg.rparent.repository / "debug" / arch

    genpkg(pkg, repo, arch, binpkg_dbg, dbgdest, True)
