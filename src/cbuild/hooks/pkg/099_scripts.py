def invoke(pkg):
    # available scripts
    _avail = [
        # "pre-install",
        # "pre-upgrade",
        # "pre-deinstall",
        # "post-install",
        # "post-upgrade",
        # "post-deinstall",
        "trigger",
    ]

    scdir = pkg.statedir / "scripts"
    scdir.mkdir(exist_ok=True)

    for h in _avail:
        scp = scdir / f"{pkg.pkgname}.{h}"
        up = pkg.rparent.template_path / f"{pkg.pkgname}.{h}"

        # scripts can be generated or can be files
        # sr = pkg.scripts.get(h, None)
        sr = None
        tp = "generated"

        if up.is_file():
            if sr is not True and h != "trigger":
                pkg.error(
                    f"undeclared script file found for '{h}'",
                    hint="try setting its field in 'scripts' variable to True",
                )
            elif isinstance(sr, str):
                pkg.error(
                    f"ambiguous script for '{h}'",
                    hint="pick either file or string but not both",
                )
            elif sr is True and h == "trigger":
                pkg.error("triggers do not need declaration in 'scripts'")
            sr = up.read_text()
            tp = "file"
        elif sr is True:
            if h == "trigger":
                pkg.error("triggers do not need declaration in 'scripts'")
            pkg.error(
                f"script file '{h}' declared in template but not found",
                hint="maybe you have a typo in the file name?",
            )

        # remove any leftovers from potential previous dirty build
        scp.unlink(missing_ok=True)

        if sr is None:
            continue

        if len(sr.strip()) == 0:
            pkg.error(f"empty script provided for '{h}'")

        if h == "trigger" and len(pkg.triggers) == 0:
            pkg.error("trigger script provided but no paths to trigger on")

        pkg.logger.out_plain(f"  \f[green]{h}:\f[] {tp}")

        with scp.open("w") as sf:
            sf.write(sr)
