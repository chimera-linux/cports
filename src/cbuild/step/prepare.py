from cbuild.core import template


def invoke(pkg):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    prepare_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepare_done"

    template.call_pkg_hooks(pkg, "init_prepare")
    template.run_pkg_func(pkg, "init_prepare")

    if prepare_done.is_file():
        return

    pkg.run_step("prepare", optional=True)

    prepare_done.touch()
