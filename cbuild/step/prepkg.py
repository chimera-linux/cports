from cbuild.core import template, dependencies

def invoke(pkg):
    crossb = pkg.rparent.cross_build if pkg.rparent.cross_build else ""
    prepkg_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepkg_done"

    if prepkg_done.is_file() and not pkg.rparent.force_mode:
        return

    template.call_pkg_hooks(pkg, "pre_pkg")
    template.run_pkg_func(pkg, "pre_pkg")

    prepkg_done.touch()
