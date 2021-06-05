from cbuild.core import paths
from cbuild import cpu

import os

def invoke(pkg):
    arch = cpu.target()
    binpkg = f"{pkg.pkgver}.{arch}.xbps"

    if pkg.repository:
        repo = os.path.join(paths.repository(), pkg.repository)
    else:
        repo = paths.repository()

    # TODO: dbg

    binpath = os.path.join(repo, binpkg)

    if os.path.isfile(binpath):
        with open(pkg.statedir / f"{pkg.pkgname}_register_pkg", "a") as f:
            f.write(f"{repo}:{binpkg}\n")
