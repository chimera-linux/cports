from cbuild.core import template


def _invoke_prepkg(pkg):
    p = pkg.rparent.profile()
    crossb = p.arch if p.cross else ""
    prepkg_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepkg_done"

    if prepkg_done.is_file() and not pkg.rparent.force_mode:
        return

    template.call_pkg_hooks(pkg, "pkg")

    prepkg_done.touch()


def invoke(pkg):
    template.call_pkg_hooks(pkg, "pkg")

    for sp in pkg.subpkg_all:
        _invoke_prepkg(sp)
