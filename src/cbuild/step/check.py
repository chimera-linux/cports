from cbuild.core import template


def invoke(pkg, step, allow_fail):
    if pkg.profile().cross:
        pkg.log("skipping check (cross build)")
        return

    if not pkg.options["check"] and not pkg._force_check:
        pkg.log("skipping check (disabled by template)")
        return

    if not pkg.run_check:
        pkg.log("skipping check (skipped by user)")
        return

    check_done = pkg.statedir / f"{pkg.pkgname}__check_done"

    template.run_pkg_func(pkg, "init_check")

    if check_done.is_file() and (not pkg.force_mode or step != "check"):
        return

    try:
        template.run_pkg_func(pkg, "pre_check")
        template.run_pkg_func(pkg, "check")
        template.run_pkg_func(pkg, "post_check")
    except Exception as e:
        if allow_fail:
            pkg.log("check failed, but proceed anyway:")
            print(e)
        else:
            raise

    check_done.touch()
