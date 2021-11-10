from cbuild.core import paths, template

import re
import shlex
import shutil
import pathlib
import subprocess

# fallback python version when we cannot determine it
def _get_pyver(pkg):
    rv = template.read_pkg(
        "python", pkg.rparent.profile().arch,
        True, False, 1, False, False, None,
        resolve = pkg.rparent, ignore_missing = True, ignore_errors = True
    )
    if not rv:
        pkg.error("failed getting python version")
    # the full version
    pv = rv.pkgver
    # reduce to just major/minor
    ld = pv.rfind(".")
    if ld > 0:
        spv = pv[0:ld]
        if spv.find(".") < 0:
            return ld
        else:
            return spv
    # should be impossible
    pkg.error(f"invalid python version ({pv})")

# every scriptlet starts with this
_header = """#!/bin/sh

set -e

"""

def _handle_catalogs(pkg, _add_hook):
    sgml_entries = []
    xml_entries = []
    catvars = {}

    for ent in pkg.sgml_entries:
        if not isinstance(ent, tuple) or len(ent) != 3:
            pkg.error("invalid SGML catalog entry")
        sgml_entries.append(ent)

    for ent in pkg.xml_entries:
        if not isinstance(ent, tuple) or len(ent) != 3:
            pkg.error("invalid XML catalog entry")
        xml_entries.append(ent)

    for catalog in pkg.sgml_catalogs:
        sgml_entries.append(("CATALOG", catalog, "--"))

    for catalog in pkg.xml_catalogs:
        xml_entries.append(("nextCatalog", catalog, "--"))

    if len(sgml_entries) > 0 or len(xml_entries) > 0:
        if len(sgml_entries) > 0:
            catvars["sgml_entries"] = " ".join(
                map(lambda v: " ".join(v), sgml_entries)
            )
        if len(xml_entries) > 0:
            catvars["xml_entries"] = " ".join(
                map(lambda v: " ".join(v), xml_entries)
            )
        # fire
        _add_hook("xml-catalog", catvars)

def _handle_accounts(pkg, _add_hook):
    # handle system groups
    if len(pkg.system_groups) > 0:
        _add_hook("system-accounts", {
            "system_groups": " ".join(pkg.system_groups)
        })

    # handle system users
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

def _handle_python(pkg, _add_hook):
    pyver = None
    pymods = []

    # python modules
    for d in (pkg.destdir / "usr/lib").glob("python*"):
        # weird?
        if not d.is_dir():
            continue
        # dig up python version from the dir
        vn = d.name[len("python"):]
        # also weird, but skip
        if not re.match(r"^[0-9]\.[0-9]+$", vn):
            continue
        # no site-packages, skip
        d = d / "site-packages"
        if not d.is_dir():
            continue
        # we know a version, make sure there are no multiples
        if pyver:
            pkg.error(f"multiple Python versions found ({pyver} and {vn})")
        pyver = vn
        if len(pkg.pycompile_modules) == 0:
            # generate implicit
            for f in d.iterdir():
                # eliminate whatever we don't want
                if f.match("*.egg-info"):
                    continue
                elif f.match("*.dist-info"):
                    continue
                elif f.match("*.so"):
                    continue
                elif f.match("*.pth"):
                    continue
                # should be ok now
                pymods.append(f.name)
        else:
            pymods = pkg.pycompile_modules

    if len(pymods) > 0 or len(pkg.pycompile_dirs) > 0:
        # version may not be obvious, in those cases figure it out
        if not pyver:
            pyver = _get_pyver(pkg)
        # export vars
        pyvars = {
            "pycompile_version": pyver
        }
        # dirs
        if len(pkg.pycompile_dirs) > 0:
            # validate first
            for d in pkg.pycompile_dirs:
                d = pathlib.Path(d)
                # must not be absolute
                if d.is_absolute():
                    pkg.error("absolute pycompile_dirs specified")
                # must exist
                if not (pkg.destdir / d).is_dir():
                    pkg.error("non-existent pycompile_dirs specified")
            # put into vars
            pyvars["pycmpile_dirs"] = " ".join(pkg.pycompile_dirs)
        # modules
        if len(pymods) > 0:
            pyvars["pycompile_module"] = " ".join(pymods)
        # add the hook
        _add_hook("pycompile", pyvars)

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

    # handle individual hooks
    _handle_accounts(pkg, _add_hook)
    _handle_catalogs(pkg, _add_hook)
    _handle_python(pkg, _add_hook)

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
