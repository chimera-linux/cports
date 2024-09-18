def invoke(pkg):
    # available scripts
    _avail = [
        "pre-install",
        "pre-upgrade",
        "pre-deinstall",
        "post-install",
        "post-upgrade",
        "post-deinstall",
        "trigger",
    ]

    scdir = pkg.statedir / "scripts"
    scdir.mkdir(exist_ok=True)

    for h in _avail:
        scp = scdir / f"{pkg.pkgname}.{h}"
        up = pkg.rparent.template_path / f"scripts/{pkg.pkgname}.{h}"

        # scripts can be generated or can be files
        sr = pkg.scripts.get(h, None)
        tp = "generated"

        if up.is_file():
            if not sr:
                sr = up.read_text()
                tp = "file"
            else:
                pkg.error(f"generated/file script conflict for '{h}', pick one")

        # remove any leftovers from potential previous dirty build
        scp.unlink(missing_ok=True)

        if not sr:
            continue

        if len(sr.strip()) == 0:
            pkg.error(f"empty script provided for '{h}'")

        if h == "trigger" and len(pkg.triggers) == 0:
            pkg.error("trigger script provided but no paths to trigger on")

        pkg.logger.out_plain(f"  \f[green]{h}:\f[] {tp}")

        with scp.open("w") as sf:
            sf.write(sr)
            pkg.log(f"added package script '{h}'")
