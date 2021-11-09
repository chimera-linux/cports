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

    # handle system groups
    if len(pkg.system_groups) > 0:
        gadd = ""
        for g in pkg.system_groups:
            gt = g.split(":")
            if len(gt) > 2 or len(gt) == 0:
                pkg.error(f"group '{g}' has invalid format")
            if len(gt) == 2:
                badgid = False
                try:
                    int(gt[1])
                except ValueError:
                    badgid = True
                if badgid or str(int(gt[1])) != gt[1]:
                    pkg.error(f"gid '{gt[1]}' is invalid")
                # basic validation done
                gadd += f"groupadd -r -g {gt[1]} '{gt[0]}' 2>/dev/null || :\n"
            else:
                gadd += f"groupadd -r '{gt[0]}' 2>/dev/null || :\n"
        # add
        if len(gadd) > 0:
            gadd = f"# add system groups\n{gadd}\n"
            _hooks["pre-install"] += gadd
            _hooks["pre-upgrade"] += gadd

    # handle system users: FIXME: only for testing for now
    # the real thing should be made into a utility script
    if len(pkg.system_users) > 0:
        uadd = ""
        udel = ""
        for u in pkg.system_users:
            uname = None
            uid = None
            uhome = "/var/empty"
            ushell = "/usr/bin/nologin"
            udesc = None
            ugroups = []
            # TODO: validation
            if isinstance(u, dict):
                uname = u["name"]
                uid = u["id"]
                if "desc" in u:
                    udesc = u["desc"]
                else:
                    udesc = f"{uname} user"
                if "shell" in u:
                    ushell = u["shell"]
                if "groups" in u:
                    ugroups = u["groups"]
                if "home" in u:
                    uhome = u["home"]
            else:
                uname, uid = u.split(":")
                uid = int(uid)
                udesc = f"{uname} user"
            # scriptlet bits
            uadd += f"useradd -r -u {uid} -c '{udesc}' -d '{uhome}' " + \
                f"-s '{ushell}' -G '{','.join(ugroups)}' {uname}" + \
                " > /dev/null 2>&1 || :\n"
            udel += f"usermod -L -d /var/empty -s /bin/false {uname}" + \
                " > /dev/null 2>&1 || :\n"
        if len(uadd) > 0:
            _hooks["pre-install"] += uadd
            _hooks["pre-upgrade"] += uadd
            _hooks["post-deinstall"] += udel

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
