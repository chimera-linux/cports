from cbuild.core import paths
from cbuild import cpu

def invoke(pkg):
    arch = cpu.target()
    binpkg = f"{pkg.pkgver}.apk"

    if pkg.repository:
        repo = paths.repository() / pkg.repository / arch
    else:
        repo = paths.repository() / arch

    # TODO: dbg

    binpath = repo / binpkg

    if binpath.is_file():
        with open(pkg.statedir / f"{pkg.rparent.pkgname}_register_pkg", "a") as f:
            f.write(f"{repo}:{binpkg}\n")
