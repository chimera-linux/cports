from cbuild.core import paths
from cbuild.util import compiler

import shutil

def _enable_wrappers(pkg):
    wrapperdir = paths.cbuild() / "wrappers"
    for f in wrapperdir.iterdir():
        if f.suffix != ".sh":
            continue
        shutil.copy2(wrapperdir / f, pkg.statedir / "wrappers" / f.stem)
        (pkg.statedir / "wrappers" / f.stem).chmod(0o755)

def _wrap_cross_cc(pkg):
    wrapperdir = paths.cbuild() / "wrappers"

    with pkg.profile("host"):
        shutil.copy2(wrapperdir / "cross-cc.c", pkg.statedir / "wrappers")
        wpath = f"/builddir/.cbuild-{pkg.pkgname}/wrappers/"
        pkg.abs_wrksrc.mkdir(exist_ok = True, parents = True)
        compiler.C(pkg).invoke(
            [wpath + "cross-cc.c"], wpath + "cross-cc", quiet = True
        )

    at = pkg.build_profile.short_triplet
    for n in ["clang", "clang++", "cc", "c++"]:
        if not (pkg.wrapperdir / f"{at}-{n}").exists():
            (pkg.wrapperdir / f"{at}-{n}").symlink_to("cross-cc")

def _wrap_cross_pkgconf(pkg):
    wdir = pkg.statedir / "wrappers"
    wfile = wdir / f"{pkg.build_profile.short_triplet}-pkg-config"
    sroot = str(pkg.build_profile.sysroot)

    with open(wfile, "w") as outf:
        outf.write(f"""#!/bin/sh

export PKG_CONFIG_SYSROOT_DIR="{sroot}"
export PKG_CONFIG_PATH="{sroot}/usr/lib/pkgconfig:{sroot}/usr/share/pkgconfig${{PKG_CONFIG_PATH:+:${{PKG_CONFIG_PATH}}}}"
export PKG_CONFIG_LIBDIR="{sroot}/usr/lib/pkgconfig${{PKG_CONFIG_LIBDIR:+:${{PKG_CONFIG_LIBDIR}}}}"
exec /usr/bin/pkg-config "$@"
""")

    wfile.chmod(0o755)

def invoke(pkg):
    _enable_wrappers(pkg)

    if not pkg.cross_build:
        return

    # wrappers for cross tools as necessary

    _wrap_cross_cc(pkg)
    _wrap_cross_pkgconf(pkg)
