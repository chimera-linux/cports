from cbuild.core import template

def invoke(pkg, step):
    crossb = pkg.cross_build if pkg.cross_build else ""
    build_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_build_done"

    template.call_pkg_hooks(pkg, "init_build")
    template.run_pkg_func(pkg, "init_build")

    if build_done.is_file() and (not pkg.rparent.force_mode or step != "build"):
        return

    pkg.run_step("build", optional = True)

    build_done.touch()
