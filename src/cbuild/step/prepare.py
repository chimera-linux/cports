from cbuild.core import template


def invoke(pkg):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    prepare_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepare_done"

    template.run_pkg_func(pkg, "init_prepare")

    if prepare_done.is_file():
        return

    template.call_pkg_hooks(pkg, "prepare")

    template.run_pkg_func(pkg, "pre_prepare")

    if hasattr(pkg, "prepare"):
        template.run_pkg_func(pkg, "prepare")

    template.run_pkg_func(pkg, "post_prepare")

    prepare_done.touch()
