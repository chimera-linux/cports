from cbuild.core import template


def invoke(pkg):
    template.call_pkg_hooks(pkg, "init_fetch")
    template.run_pkg_func(pkg, "init_fetch")

    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    fetch_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_fetch_done"
    if fetch_done.is_file():
        return

    template.call_pkg_hooks(pkg, "pre_fetch")
    template.run_pkg_func(pkg, "pre_fetch")

    if hasattr(pkg, "do_fetch"):
        pkg.cwd.mkdir(parents=True, exist_ok=True)
        template.run_pkg_func(pkg, "do_fetch")
    else:
        template.call_pkg_hooks(pkg, "do_fetch")

    template.run_pkg_func(pkg, "post_fetch")
    template.call_pkg_hooks(pkg, "post_fetch")

    fetch_done.touch()
