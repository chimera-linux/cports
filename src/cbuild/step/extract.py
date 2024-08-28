from cbuild.core import template


def invoke(pkg):
    template.run_pkg_func(pkg, "init_extract")

    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    extract_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_extract_done"
    if extract_done.is_file():
        return

    template.run_pkg_func(pkg, "pre_extract")

    if hasattr(pkg, "extract"):
        template.run_pkg_func(pkg, "extract")
    else:
        template.call_pkg_hooks(pkg, "extract")

    pkg.srcdir.mkdir(parents=True, exist_ok=True)

    template.run_pkg_func(pkg, "post_extract")

    extract_done.touch()
