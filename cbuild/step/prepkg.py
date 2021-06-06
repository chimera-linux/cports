from cbuild.core import template, dependencies

def invoke(pkg):
    prepkg_done = pkg.statedir / f"{pkg.pkgname}__prepkg_done"

    if prepkg_done.is_file() and not pkg.rparent.force_mode:
        return

    pkg.run_depends = dependencies.get_pkg_depends(pkg, False)
    template.call_pkg_hooks(pkg, "pre_pkg")

    prepkg_done.touch()
