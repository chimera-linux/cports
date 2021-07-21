from cbuild.core import template

def invoke(pkg, step):
    if pkg.cross_build:
        pkg.log("skipping check (cross build)")
        return

    if not pkg.options["check"]:
        pkg.log("skipping check (disabled by template)")
        return

    if not pkg.run_check:
        pkg.log("skipping check (skipped by user)")
        return

    check_done = pkg.statedir / f"{pkg.pkgname}__check_done"

    template.call_pkg_hooks(pkg, "init_check")
    template.run_pkg_func(pkg, "init_check")

    if check_done.is_file() and (not pkg.rparent.force_mode or step != "check"):
        return

    pkg.run_step("check", optional = True)

    check_done.touch()
