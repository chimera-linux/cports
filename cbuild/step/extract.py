from cbuild.core import template

import os

def invoke(pkg):
    template.call_pkg_hooks(pkg, "init_extract")
    template.run_pkg_func(pkg, "init_extract")

    extract_done = pkg.statedir / f"{pkg.pkgname}__extract_done"
    if extract_done.is_file():
        return

    template.call_pkg_hooks(pkg, "pre_extract")
    template.run_pkg_func(pkg, "pre_extract")

    if hasattr(pkg, "do_extract"):
        os.makedirs(pkg.abs_wrksrc, exist_ok = True)
        template.run_pkg_func(pkg, "do_extract")
    else:
        template.call_pkg_hooks(pkg, "do_extract")

    template.run_pkg_func(pkg, "post_extract")
    template.call_pkg_hooks(pkg, "post_extract")

    extract_done.touch()
