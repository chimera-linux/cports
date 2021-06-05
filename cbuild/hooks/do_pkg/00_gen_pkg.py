from cbuild.core import logger, paths

from cbuild import cpu

import os
import glob
import time
import subprocess

def genpkg(pkg, repo, arch, binpkg):
    if not os.path.isdir(pkg.destdir):
        pkg.log_warn(f"cannot find pkg destdir, skipping...")
        return

    binpath = os.path.join(repo, binpkg)
    lockpath = binpath + ".lock"

    os.makedirs(repo, exist_ok = True)

    while os.path.isfile(lockpath):
        pkg.log_warn(f"binary package being created, waiting...")
        time.sleep(1)

    # don't overwrite by default
    if os.path.isfile(binpath) and not pkg.rparent.force_mode:
        pkg.log_warn(f"skipping existing {binpkg}...")
        return

    rc = 0
    try:
        open(lockpath, "w").close()

        args = []

        if len(pkg.provides) > 0:
            args.append("--provides")
            args.append(" ".join(pkg.provides))

        if len(pkg.conflicts) > 0:
            args.append("--conflicts")
            args.append(" ".join(pkg.conflicts))

        if len(pkg.replaces) > 0:
            args.append("--replaces")
            args.append(" ".join(pkg.replaces))

        if len(pkg.reverts) > 0:
            args.append("--reverts")
            args.append(" ".join(pkg.reverts))

        if len(pkg.mutable_files) > 0:
            args.append("--mutable-files")
            args.append(" ".join(pkg.mutable_files))

        if os.path.isfile(os.path.join(pkg.destdir, "rdeps")):
            with open(os.path.join(pkg.destdir, "rdeps")) as f:
                rdeps = f.read()
                if len(rdeps) > 0:
                    args.append("--dependencies")
                    args.append(rdeps)

        cf = []
        for c in pkg.conf_files:
            for g in glob.glob(str(pkg.destdir / os.path.relpath(c, "/"))):
                cf.append(os.path.relpath(g, pkg.destdir))

        if len(cf) > 0:
            args.append("--config-files")
            args.append(" ".join(cf))

        if os.path.isfile(os.path.join(pkg.statedir, "gitrev")):
            with open(os.path.join(pkg.statedir, "gitrev")) as f:
                grevs = f.read()
                if len(grevs) > 0:
                    args.append("--source-revisions")
                    args.append(grevs)

        if os.path.isfile(os.path.join(pkg.destdir, "shlib-provides")):
            with open(os.path.join(pkg.destdir, "shlib-provides")) as f:
                shp = f.read()
                if len(shp) > 0:
                    args.append("--shlib-provides")
                    args.append(shp)

        if os.path.isfile(os.path.join(pkg.destdir, "shlib-requires")):
            with open(os.path.join(pkg.destdir, "shlib-requires")) as f:
                shp = f.read()
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

        if pkg.changelog:
            args.append("--changelog")
            args.append(pkg.changelog)

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

        logger.get().out(f"Creating {binpkg} in repository {repo}...")

        os.chdir(repo)
        rc = subprocess.run(["xbps-create"] + args).returncode
    finally:
        os.unlink(lockpath)
        os.chdir(paths.distdir())

        if rc != 0:
            if os.path.isfile(binpath):
                os.unlink(binpath)
            pkg.error("failed to create {binpkg}")

def invoke(pkg):
    arch = cpu.target()
    binpkg = f"{pkg.pkgver}.{arch}.xbps"

    if pkg.repository:
        repo = os.path.join(paths.repository(), pkg.repository)
    else:
        repo = paths.repository()

    genpkg(pkg, repo, arch, binpkg)

    for sp in pkg.rparent.subpkg_list:
        if sp.pkgname == f"{pkg.rparent.pkgname}-dbg":
            return

    # TODO: dbg
