from cbuild.core import paths

import shlex
import shutil
import subprocess

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

    # executable hooks to invoke
    _reghooks = {}

    def _add_hook(hookn, evars):
        if hookn in _reghooks:
            _reghooks[hookn].update(evars)
        else:
            _reghooks[hookn] = evars

    # handle system groups
    if len(pkg.system_groups) > 0:
        _add_hook("system-accounts", {
            "system_groups": " ".join(pkg.system_groups)
        })

    # handle system users: FIXME: only for testing for now
    # the real thing should be made into a utility script
    if len(pkg.system_users) > 0:
        evars = {}
        usrs = []
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
                # the form can be with or without id
                if uid:
                    usrs.append(f"{uname}:{uid}")
                else:
                    usrs.append(uname)
                # optional fields
                if "home" in u:
                    evars[f"{uname}_homedir"] = u["home"]
                if "shell" in u:
                    evars[f"{uname}_shell"] = u["shell"]
                if "desc" in u:
                    evars[f"{uname}_descr"] = u["desc"]
                if "groups" in u:
                    evars[f"{uname}_groups"] = ",".join(u["groups"])
                if "pgroup" in u:
                    evars[f"{uname}_pgroup"] = u["pgroup"]
            else:
                usrs.append(u)
            # add the main var
            evars["system_users"] = " ".join(usrs)
        # add the hook
        _add_hook("system-accounts", evars)

    hookpath = paths.distdir() / "main/apk-chimera-hooks/files"

    # add executable scriptlets
    for h in _reghooks:
        envs = _reghooks[h]
        # go through every target
        for tgt in subprocess.run(
            ["sh", hookpath / h, "targets"], capture_output = True,
            check = True
        ).stdout.decode().strip().split():
            if not tgt in _hooks:
                # this should never happen unless we are buggy
                pkg.error(f"unknown hook: {tgt}")
            # export env vars for the hook
            for e in envs:
                _hooks[tgt] += f"export {e}={shlex.quote(envs[e])}\n"
            # insert the hook
            pkg.log(f"added hook '{h}' for scriptlet '{tgt}'")
            _hooks[tgt] += f"/usr/libexec/apk-chimera-hooks/{h} run {tgt} " + \
                           f"'{pkg.pkgname}' '{pkg.pkgver}'\n"

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
            # log
            pkg.log(f"added package scriptlet '{h}'")

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
        with open(scdir / f"{pkg.pkgname}.{h}", "w") as sf:
            sf.write(_header)
            sf.write(s)
            sf.write("\n")
