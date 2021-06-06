def invoke(pkg, step):
    configure_done = pkg.statedir / f"{pkg.pkgname}__configure_done"

    if configure_done.is_file() and (
        not pkg.rparent.force_mode or step != "configure"
    ):
        return

    pkg.run_step("configure", optional = True)

    configure_done.touch()
