from cbuild.core import logger, paths

from cbuild import cpu

import os
import glob
import time
import pathlib
import subprocess

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

    # don't overwrite by default
    if binpath.is_file() and not pkg.rparent.force_mode:
        pkg.log_warn(f"skipping existing {binpkg}...")
        return

    rc = 0
    try:
        lockpath.touch()

        args = []

        if len(pkg.provides) > 0:
            args.append("--provides")
            args.append(" ".join(pkg.provides))

        if len(pkg.conflicts) > 0:
            args.append("--conflicts")
            args.append(" ".join(pkg.conflicts))

        if len(pkg.mutable_files) > 0:
            args.append("--mutable-files")
            args.append(" ".join(pkg.mutable_files))

        if (pkg.destdir / "rdeps").is_file():
            rdeps = (pkg.destdir / "rdeps").read_text().strip()
            if len(rdeps) > 0:
                args.append("--dependencies")
                args.append(rdeps)

        cf = []
        for c in pkg.conf_files:
            for g in glob.glob(
                str(pkg.destdir / pathlib.Path(c).relative_to("/"))
            ):
                cf.append(str(pathlib.Path(g).relative_to(pkg.destdir)))

        if len(cf) > 0:
            args.append("--config-files")
            args.append(" ".join(cf))

        if (pkg.statedir / "gitrev").is_file():
            grevs = (pkg.statedir / "gitrev").read_text().strip()
            if len(grevs) > 0:
                args.append("--source-revisions")
                args.append(grevs)

        if (pkg.destdir / "shlib-provides").is_file():
            shp = (pkg.destdir / "shlib-provides").read_text().strip()
            if len(shp) > 0:
                args.append("--shlib-provides")
                args.append(shp)

        if (pkg.destdir / "shlib-requires").is_file():
            shp = (pkg.destdir / "shlib-requires").read_text().strip()
            if len(shp) > 0:
                args.append("--shlib-requires")
                args.append(shp)

        if len(pkg.alternatives) > 0:
            args.append("--alternatives")
            args.append(" ".join([":".join(v) for v in pkg.alternatives]))

        if pkg.preserve:
            args.append("--preserve")

        if len(pkg.tags) > 0:
            args.append("--tags")
            args.append(" ".join(pkg.tags))

        if pkg.rparent.changelog:
            args.append("--changelog")
            args.append(pkg.rparent.changelog)

        args.append("--architecture")
        args.append(arch)

        args.append("--homepage")
        args.append(pkg.rparent.homepage)

        args.append("--license")
        args.append(pkg.rparent.license)

        args.append("--maintainer")
        args.append(pkg.rparent.maintainer)

        args.append("--desc")
        args.append(pkg.short_desc)

        args.append("--pkgver")
        args.append(pkg.pkgver)

        args.append("--quiet")

        args.append(pkg.destdir)

        logger.get().out(f"Creating {binpkg} in repository {str(repo)}...")

        os.chdir(repo)
        rc = subprocess.run(["xbps-create"] + args).returncode
    finally:
        lockpath.unlink()
        os.chdir(paths.distdir())

        if rc != 0:
            binpath.unlink(missing_ok = True)
            pkg.error("failed to create {binpkg}")

def invoke(pkg):
    arch = cpu.target()
    binpkg = f"{pkg.pkgver}.{arch}.xbps"

    if pkg.repository:
        repo = paths.repository() / pkg.repository
    else:
        repo = paths.repository()

    genpkg(pkg, repo, arch, binpkg)

    for sp in pkg.rparent.subpkg_list:
        if sp.pkgname == f"{pkg.rparent.pkgname}-dbg":
            return

    # TODO: dbg
