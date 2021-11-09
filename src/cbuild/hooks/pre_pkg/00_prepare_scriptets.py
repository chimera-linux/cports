import shutil

# every scriptlet starts with this
_header = """#!/bin/sh

set -e

"""

def invoke(pkg):
    # base
    _hooks = {
        "pre-install": "",
        "pre-upgrade": "",
        "pre-deinstall": "",
        "post-install": "",
        "post-upgrade": "",
        "post-deinstall": "",
        "trigger": ""
    }

    # add user scriptlets
    for h in _hooks:
        up = pkg.rparent.template_path / f"{pkg.pkgname}.{h}"
        if up.is_file():
            # read entire thing into the buffer
            sr = up.read_text()
            # strip shebang
            if sr.startswith("#!"):
                nl = sr.find("\n")
                if nl < 0:
                    # no newline found so it was just a comment
                    sr = ""
                else:
                    sr = sr[nl + 1:].strip()
            # append cleared up scriptlet
            if len(sr) > 0:
                _hooks[h] += "# package script\n\n"
                _hooks[h] += sr

    # set up scriptlet dir
    scdir = pkg.statedir / "scriptlets"
    if scdir.is_dir():
        shutil.rmtree(scdir)
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
        with open(scdir / f".{h}", "w") as sf:
            sf.write(_header)
            sf.write(s)
            sf.write("\n")
