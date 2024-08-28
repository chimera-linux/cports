from cbuild.core import template


def invoke(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    build_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_build_done"

    template.run_pkg_func(pkg, "init_build")

    if build_done.is_file() and (not pkg.force_mode or step != "build"):
        return

    template.run_pkg_func(pkg, "pre_build")
    template.run_pkg_func(pkg, "build")
    template.run_pkg_func(pkg, "post_build")

    build_done.touch()
