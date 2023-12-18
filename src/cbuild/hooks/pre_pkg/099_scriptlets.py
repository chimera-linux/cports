def invoke(pkg):
    # base
    _hooks = {
        "pre-install": "",
        "pre-upgrade": "",
        "pre-deinstall": "",
        "post-install": "",
        "post-upgrade": "",
        "post-deinstall": "",
        "trigger": "",
    }

    # add user scriptlets
    for h in _hooks:
        up = pkg.rparent.template_path / f"{pkg.pkgname}.{h}"
        # scriptlets can be generated or can be files
        if h in pkg.scriptlets:
            sr = pkg.scriptlets[h]
        elif up.is_file():
            # read entire thing into the buffer
            sr = up.read_text()
        else:
            sr = None
        if sr:
            # strip shebang
            if sr.startswith("#!"):
                nl = sr.find("\n")
                if nl < 0:
                    # no newline found so it was just a comment
                    sr = ""
                else:
                    sr = sr[nl + 1 :].strip()
            # append cleared up scriptlet
            if len(sr) > 0:
                _hooks[h] += "# package script\n"
                _hooks[h] += "set -e\n\n"
                _hooks[h] += sr
            # log
            pkg.log(f"added package scriptlet '{h}'")

    # set up scriptlet dir
    scdir = pkg.statedir / "scriptlets"
    if scdir.is_dir():
        # remove potential leftovers for this package
        for sc in scdir.glob(f"{pkg.pkgname}.*"):
            sc.unlink()
    else:
        scdir.mkdir()

    # generate
    for h in _hooks:
        s = _hooks[h].strip()
        # got nothing, do not generate
        if len(s) == 0:
            continue
        # for triggers, ensure we trigger on something
        if h == "trigger" and len(pkg.triggers) == 0:
            pkg.error("trigger scriptlet provided but no triggers")
        # create file
        with open(scdir / f"{pkg.pkgname}.{h}", "w") as sf:
            sf.write("#!/bin/sh\n\n")
            sf.write(s)
            sf.write("\n")
