def invoke(pkg, step):
    build_done = pkg.statedir / f"{pkg.pkgname}__build_done"

    if build_done.is_file() and (not pkg.rparent.force_mode or step != "build"):
        return

    pkg.run_step("build", optional = True)

    build_done.touch()
