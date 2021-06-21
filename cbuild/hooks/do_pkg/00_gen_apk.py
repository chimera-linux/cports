from cbuild.core import logger, paths
from cbuild.apk import create as apk_c, sign as apk_s

from cbuild import cpu

import os
import glob
import time
import pathlib
import subprocess

_hooks = [
    "pre-install", "post-install",
    "pre-upgrade", "post-upgrade",
    "pre-deinstall", "post-deinstall"
]

def genpkg(pkg, repo, arch, binpkg):
    if not pkg.destdir.is_dir():
        pkg.log_warn(f"cannot find pkg destdir, skipping...")
        return

    binpath = repo / binpkg
    lockpath = binpath.with_suffix(binpath.suffix + ".lock")

    os.makedirs(repo, exist_ok = True)

    while lockpath.is_file():
        pkg.log_warn(f"binary package being created, waiting...")
        time.sleep(1)

    try:
        lockpath.touch()

        metadata = {}
        args = []

        metadata["pkgdesc"] = pkg.short_desc
        metadata["url"] = pkg.rparent.homepage
        metadata["maintainer"] = pkg.rparent.maintainer
        #metadata["packager"] = pkg.rparent.maintainer
        metadata["origin"] = pkg.rparent.pkgname
        metadata["license"] = pkg.rparent.license
        # TODO: remove changelog, tags, conf_files; add remaining apk stuff

        if pkg.rparent.git_revision:
            metadata["commit"] = pkg.rparent.git_revision + (
                "-dirty" if pkg.rparent.git_dirty else ""
            )

        if len(pkg.provides) > 0:
            metadata["provides"] = pkg.provides

        mdeps = []

        for c in pkg.conflicts:
            mdeps.append("!" + c)
        for c in pkg.depends:
            mdeps.append(c)

        metadata["depends"] = mdeps

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

        logger.get().out(f"Creating {binpkg} in repository {str(repo)}...")

        apk_c.create(
            pkg.pkgname, pkg.version + "-r" + str(pkg.revision), arch,
            pkg.rparent.source_date_epoch, pkg.destdir, pkg.statedir, binpath,
            pkg.rparent.signing_key, metadata
        )
    finally:
        lockpath.unlink()

def invoke(pkg):
    arch = cpu.target()
    binpkg = f"{pkg.pkgver}.apk"

    if pkg.repository:
        repo = paths.repository() / pkg.repository / arch
    else:
        repo = paths.repository() / arch

    genpkg(pkg, repo, arch, binpkg)

    for sp in pkg.rparent.subpkg_list:
        if sp.pkgname == f"{pkg.rparent.pkgname}-dbg":
            return

    # TODO: dbg
