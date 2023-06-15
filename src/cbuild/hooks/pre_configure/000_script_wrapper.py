from cbuild.core import paths

import shutil


def _enable_wrappers(pkg):
    wrapperdir = paths.cbuild() / "wrappers"
    for f in wrapperdir.iterdir():
        if f.suffix != ".sh":
            continue
        shutil.copy2(wrapperdir / f, pkg.statedir / "wrappers" / f.stem)
        (pkg.statedir / "wrappers" / f.stem).chmod(0o755)

    for src, name in pkg.exec_wrappers:
        wpath = pkg.statedir / "wrappers" / name
        wpath.unlink(missing_ok=True)
        wpath.symlink_to(src)


def _wrap_cross_cc(pkg):
    at = pkg.profile().triplet
    for n in ["clang", "clang++", "cc", "c++"]:
        if not (pkg.wrapperdir / f"{at}-{n}").is_symlink():
            (pkg.wrapperdir / f"{at}-{n}").symlink_to(
                "/usr/bin/cbuild-cross-cc"
            )


def _wrap_cross_pkgconf(pkg):
    wdir = pkg.statedir / "wrappers"
    wfile = wdir / f"{pkg.profile().triplet}-pkg-config"
    sroot = str(pkg.profile().sysroot)

    with open(wfile, "w") as outf:
        outf.write(
            f"""#!/bin/sh

export PKG_CONFIG_SYSROOT_DIR="{sroot}"
export PKG_CONFIG_PATH="{sroot}/usr/lib/pkgconfig:{sroot}/usr/share/pkgconfig${{PKG_CONFIG_PATH:+:${{PKG_CONFIG_PATH}}}}"
export PKG_CONFIG_LIBDIR="{sroot}/usr/lib/pkgconfig${{PKG_CONFIG_LIBDIR:+:${{PKG_CONFIG_LIBDIR}}}}"
exec /usr/bin/pkg-config "$@"
"""
        )

    wfile.chmod(0o755)


def invoke(pkg):
    _enable_wrappers(pkg)

    if not pkg.profile().cross:
        return

    # wrappers for cross tools as necessary

    _wrap_cross_cc(pkg)
    _wrap_cross_pkgconf(pkg)
