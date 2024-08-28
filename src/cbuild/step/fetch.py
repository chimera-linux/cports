from cbuild.core import template, paths
from cbuild.util import flock


def _invoke(pkg):
    template.run_pkg_func(pkg, "init_fetch")

    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    fetch_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_fetch_done"
    if fetch_done.is_file():
        return

    template.run_pkg_func(pkg, "pre_fetch")

    if hasattr(pkg, "fetch"):
        pkg.cwd.mkdir(parents=True, exist_ok=True)
        template.run_pkg_func(pkg, "fetch")
    else:
        template.call_pkg_hooks(pkg, "fetch")

    template.run_pkg_func(pkg, "post_fetch")

    fetch_done.touch()


def invoke(pkg):
    srclock = paths.sources() / "cbuild.lock"

    # lock the whole sources dir for the operation
    #
    # while a per-template lock may seem enough,
    # that would still race when sharing sources
    # between templates (which regularly happens)
    with flock.lock(srclock, pkg):
        _invoke(pkg)
