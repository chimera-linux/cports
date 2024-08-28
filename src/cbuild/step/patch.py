from cbuild.core import template


def invoke(pkg):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    patch_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_patch_done"

    template.run_pkg_func(pkg, "init_patch")

    if patch_done.is_file():
        return

    template.run_pkg_func(pkg, "pre_patch")

    if hasattr(pkg, "patch"):
        template.run_pkg_func(pkg, "patch")
    else:
        template.call_pkg_hooks(pkg, "patch")

    template.run_pkg_func(pkg, "post_patch")

    patch_done.touch()
