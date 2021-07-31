from cbuild.core import paths

def invoke(pkg):
    arch = pkg.rparent.build_profile.arch
    binpkg = f"{pkg.pkgver}.apk"
    binpkg_dbg = f"{pkg.pkgname}-dbg-{pkg.version}-r{pkg.revision}.apk"

    if pkg.repository:
        repo = paths.repository() / pkg.repository / arch
    else:
        repo = paths.repository() / arch

    binpath = repo / binpkg

    if binpath.is_file():
        with open(pkg.statedir / f"{pkg.rparent.pkgname}_register_pkg", "a") as f:
            f.write(f"{repo}:{binpkg}\n")

    repo = paths.repository() / "debug" / arch
    binpath = repo / binpkg_dbg

    if not binpath.is_file():
        return

    if not (
        pkg.rparent.destdir_base / f"{pkg.pkgname}-dbg-{pkg.version}"
    ).is_dir():
        return

    with open(pkg.statedir / f"{pkg.rparent.pkgname}_register_pkg", "a") as f:
        f.write(f"{repo}:{binpkg_dbg}\n")
