from cbuild.core import template


def invoke(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    cfg_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_configure_done"

    template.run_pkg_func(pkg, "init_configure")

    if cfg_done.is_file() and (not pkg.force_mode or step != "configure"):
        return

    template.run_pkg_func(pkg, "pre_configure")
    template.run_pkg_func(pkg, "configure")
    template.run_pkg_func(pkg, "post_configure")

    cfg_done.touch()
