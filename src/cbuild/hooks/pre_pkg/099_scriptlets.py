import io
import shlex

# hooks for xml/sgml registration

_xml_register_entries = r"""
local sgml_catalog=/etc/sgml/auto/catalog
local xml_catalog=/etc/xml/auto/catalog

[ -n "${sgml_entries}" -a ! -f "${sgml_catalog}" ] && return 0
[ -n "${xml_entries}" -a ! -f "${xml_catalog}" ] && return 0

if [ -n "${sgml_entries}" ]; then
    echo -n "Registering SGML catalog entries... "
    set -- ${sgml_entries}
    while [ $# -gt 0 ]; do
        /usr/bin/xmlcatmgr -sc ${sgml_catalog} add "$1" "$2" "$3"
        shift; shift; shift;
    done
    echo "done."
fi

if [ -n "${xml_entries}" ]; then
    echo -n "Registering XML catalog entries... "
    set -- ${xml_entries}
    while [ $# -gt 0 ]; do
        /usr/bin/xmlcatmgr -c ${xml_catalog} add "$1" "$2" "$3"
        shift; shift; shift;
    done
    echo "done."
fi
"""

_xml_unregister_entries = r"""
local sgml_catalog=/etc/sgml/auto/catalog
local xml_catalog=/etc/xml/auto/catalog

[ -n "${sgml_entries}" -a ! -f "${sgml_catalog}" ] && return 0
[ -n "${xml_entries}" -a ! -f "${xml_catalog}" ] && return 0

if [ -n "${sgml_entries}" ]; then
    echo -n "Unregistering SGML catalog entries... "
    set -- ${sgml_entries}
    while [ $# -gt 0 ]; do
        /usr/bin/xmlcatmgr -sc ${sgml_catalog} remove "$1" "$2" \
            2>/dev/null
        shift; shift; shift
    done
    echo "done."
fi
if [ -n "${xml_entries}" ]; then
    echo -n "Unregistering XML catalog entries... "
    set -- ${xml_entries}
    while [ $# -gt 0 ]; do
        /usr/bin/xmlcatmgr -c ${xml_catalog} remove "$1" "$2" \
            2>/dev/null
        shift; shift; shift
    done
    echo "done."
fi
"""

# hooks for account setup

_acct_setup = r"""
local USERADD USERMOD

[ -z "$system_users" -a -z "$system_groups" ] && return 0

if command -v useradd >/dev/null 2>&1; then
    USERADD="useradd"
fi

if command -v usermod >/dev/null 2>&1; then
    USERMOD="usermod"
fi

show_acct_details() {
    echo "   Account: $1"
    echo "   Description: '$2'"
    echo "   Homedir: '$3'"
    echo "   Shell: '$4'"
    [ -n "$5" ] && echo "   Additional groups: '$5'"
}

group_add() {
    local _pretty_grname _grname _gid

    if ! command -v groupadd >/dev/null 2>&1; then
        echo "WARNING: cannot create $1 system group (missing groupadd)"
        echo "The following group must be created manually: $1"
        return 0
    fi

    _grname="${1%:*}"
    _gid="${1##*:}"

    [ "${_grname}" = "${_gid}" ] && _gid=

    _pretty_grname="${_grname}${_gid:+ (gid: ${_gid})}"

    groupadd -r ${_grname} ${_gid:+-g ${_gid}} >/dev/null 2>&1

    case $? in
        0) echo "Created ${_pretty_grname} system group." ;;
        9) ;;
        *) echo "ERROR: failed to create system group ${_pretty_grname}!"; return 1;;
    esac

    return 0
}

# System groups required by a package.
for grp in ${system_groups}; do
    group_add $grp || return 1
done

# System user/group required by a package.
for acct in ${system_users}; do
    _uname="${acct%:*}"
    _uid="${acct##*:}"

    [ "${_uname}" = "${_uid}" ] && _uid=

    eval homedir="\$${_uname}_homedir"
    eval shell="\$${_uname}_shell"
    eval descr="\$${_uname}_descr"
    eval groups="\$${_uname}_groups"
    eval pgroup="\$${_uname}_pgroup"

    [ -z "$homedir" ] && homedir="/var/empty"
    [ -z "$shell" ] && shell="/usr/bin/nologin"
    [ -z "$descr" ] && descr="${_uname} user"
    [ -n "$groups" ] && user_groups="-G $groups"

    if [ -n "${_uid}" ]; then
        use_id="-u ${_uid} -g ${pgroup:-${_uid}}"
        _pretty_uname="${_uname} (uid: ${_uid})"
    else
        use_id="-g ${pgroup:-${_uname}}"
        _pretty_uname="${_uname}"
    fi

    if [ -z "$USERADD" -o -z "$USERMOD" ]; then
        echo "WARNING: cannot create ${_uname} system account (missing useradd or usermod)"
        echo "The following system account must be created:"
        show_acct_details "${_pretty_uname}" "${descr}" "${homedir}" "${shell}" "${groups}"
        continue
    fi

    group_add ${pgroup:-${acct}} || return 1

    ${USERADD} -c "${descr}" -d "${homedir}" \
        ${use_id} ${pgroup:+-N} -s "${shell}" \
        ${user_groups} -r ${_uname} >/dev/null 2>&1

    case $? in
        0)
            echo "Created ${_pretty_uname} system user."
            ${USERMOD} -L ${_uname} >/dev/null 2>&1
            if [ $? -ne 0 ]; then
                echo "WARNING: unable to lock password for ${_uname} system account"
            fi
            ;;
        9)
            ${USERMOD} -c "${descr}" -d "${homedir}" \
                -s "${shell}" -g "${pgroup:-${_uname}}" \
                ${user_groups} ${_uname} >/dev/null 2>&1
            if [ $? -eq 0 ]; then
                echo "Updated ${_uname} system user."
            else
                echo "WARNING: unable to modify ${_uname} system account"
                echo "Please verify that account is compatible with these settings:"
                show_acct_details "${_pretty_uname}" \
                    "${descr}" "${homedir}" "${shell}" "${groups}"
                continue
            fi
            ;;
        *)
            echo "ERROR: failed to create system user ${_pretty_uname}!"
            return 1
            ;;
    esac
done
"""

_acct_drop = r"""
local USERMOD

[ -z "$system_users" ] && return 0

if command -v usermod >/dev/null 2>&1; then
    USERMOD="usermod"
fi

for acct in ${system_users}; do
    _uname="${acct%:*}"

    comment="$( (getent passwd "${_uname}" | cut -d: -f5 | head -n1) 2>/dev/null )"
    comment="${comment:-user} - removed package ${1}"

    if [ -z "$USERMOD" ]; then
        echo "WARNING: cannot disable ${_uname} system user (missing usermod)"
        continue
    fi

    ${USERMOD} -L -d /var/empty -s /usr/bin/false \
        -c "${comment}" ${_uname} >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Disabled ${_uname} system user."
    fi
done
"""

# all known hook scriptlets

_hookscripts = {
    "xml_catalog": {
        "post-install": _xml_register_entries,
        "post-upgrade": _xml_register_entries,
        "pre-deinstall": _xml_unregister_entries,
        "pre-upgrade": _xml_unregister_entries,
    },
    "system_accounts": {
        "pre-install": _acct_setup,
        "pre-upgrade": _acct_setup,
        "post-deinstall": _acct_drop,
    },
}


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
        _add_hook("xml_catalog", catvars)


def _handle_accounts(pkg, _add_hook):
    # handle system groups
    if len(pkg.system_groups) > 0:
        _add_hook(
            "system_accounts", {"system_groups": " ".join(pkg.system_groups)}
        )

    # handle system users
    if len(pkg.system_users) > 0:
        evars = {}
        usrs = []
        for u in pkg.system_users:
            uname = None
            uid = None
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
        _add_hook("system_accounts", evars)


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

    # add executable scriptlets
    for h in _reghooks:
        envs = _reghooks[h]
        # go through every target
        for tgt in _hookscripts[h]:
            if tgt not in _hooks:
                # this should never happen unless we are buggy
                pkg.error(f"unknown hook: {tgt}")
            # export env vars for the hook
            for e in envs:
                _hooks[tgt] += f"{e}={shlex.quote(envs[e])}\n"
            # export the scriptlet as function
            _hooks[tgt] += f"\n_{h}_invoke() " + "{\n"
            for ln in io.StringIO(_hookscripts[h][tgt]):
                # empty lines
                if len(ln.strip()) == 0:
                    _hooks[tgt] += "\n"
                    continue
                # add the line, indent as needed
                _hooks[tgt] += f"    {ln.rstrip()}\n"
            # end the function
            _hooks[tgt] += "    return 0\n}\n"
            # insert the hook
            pkg.log(f"added hook '{h}' for scriptlet '{tgt}'")
            _hooks[tgt] += (
                f"_{h}_invoke '{pkg.pkgname}' '{pkg.pkgver}'" + " || exit $?\n"
            )

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
