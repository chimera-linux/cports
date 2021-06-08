from cbuild.core import template, dependencies

def invoke(pkg):
    prepkg_done = pkg.statedir / f"{pkg.pkgname}__prepkg_done"

    if prepkg_done.is_file() and not pkg.rparent.force_mode:
        return

    pkg.run_depends = list(pkg.depends)
    template.call_pkg_hooks(pkg, "pre_pkg")

    prepkg_done.touch()
