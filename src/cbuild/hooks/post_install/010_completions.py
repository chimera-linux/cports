def invoke(pkg):
    comps = []

    if (
        compspath := pkg.destdir / "usr/share/fish/vendor_completions.d"
    ).is_dir():
        comps.extend(
            (f, f.name.removesuffix(".fish")) for f in compspath.iterdir()
        )

    if (compspath := pkg.destdir / "usr/share/zsh/site-functions").is_dir():
        comps.extend(
            (f, f.name[1:])
            for f in compspath.iterdir()
            if f.name.startswith("_")
        )

    if (
        pkg.pkgname != "bash-completion"
        and (
            compspath := pkg.destdir / "usr/share/bash-completion/completions"
        ).is_dir()
    ):
        comps.extend((f, f.name) for f in compspath.iterdir())

    # we skip checking nushell comps because the dir to which they get installed
    # is for auto-loaded functions in general and not just comps, and there's no
    # robust way to distinguish them (zsh does the same but zsh completions have
    # a _ prefix so it's ok)

    if (binpath := pkg.destdir / "usr/bin").is_dir():
        commands = {f.name for f in binpath.iterdir()}
    else:
        commands = set()

    fail = False

    for comppath, compname in comps:
        if compname not in commands:
            pkg.log_red(
                f"completion file {comppath.relative_to(pkg.destdir)} has no matching usr/bin binary"
            )
            fail = True

    if fail:
        pkg.error("completions check failed")
