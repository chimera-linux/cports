from cbuild.core import template

def invoke(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    configure_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_configure_done"

    template.call_pkg_hooks(pkg, "init_configure")
    template.run_pkg_func(pkg, "init_configure")

    if configure_done.is_file() and (
        not pkg.rparent.force_mode or step != "configure"
    ):
        return

    pkg.run_step("configure", optional = True)

    configure_done.touch()
