# prepares /etc/passwd and /etc/group as needed to generate packages

from cbuild.core import chroot, paths

import shlex


def invoke(pkg):
    # don't involve users during bootstrap
    if pkg.stage < 1:
        return

    # assert this, should always be true...
    if not (paths.bldroot() / "usr/bin/sd-sysusers").exists():
        pkg.error("sd-sysusers not present in chroot")

    glist = []
    ulist = []

    # add new groups
    for g in pkg.system_groups:
        gl = g.split(":")
        if len(gl) == 1:
            gname = g
            gid = "-"
        else:
            gname = gl[0]
            gid = gl[1]
        glist.append(f"g {gname} {gid}")

    # add new users
    for u in pkg.system_users:
        if isinstance(u, dict):
            uname = u["name"]
            uid = u["id"]
            if not uid:
                uid = "-"
            # home dir
            if "home" in u:
                uhm = u["home"]
            else:
                uhm = "/tmp"
            # comment
            if "desc" in u:
                ucmt = u["desc"]
            else:
                ucmt = f"{uname} user"
            # shell
            if "shell" in u:
                ush = u["shell"]
            else:
                ush = "/bin/sh"
            # primary gid
            if "pgroup" in u:
                gn = u["pgroup"]
            else:
                gn = None
        else:
            ul = u.split(":")
            if len(ul) == 1:
                uname = u
                uid = "-"
            else:
                uname = ul[0]
                uid = ul[1]
            # remaining info is automatic
            gn = None
            uhm = "/tmp"
            ucmt = f"{uname} user"
            ush = "/bin/sh"
        if gn:
            uid = f"{uid}:{gn}"
        ulist.append(f"u {uname} {uid} {shlex.quote(ucmt)} {uhm} {ush}")

    # generate sysusers file
    with open(paths.bldroot() / "usr/lib/sysusers.d/cbuild.conf", "w") as outf:
        for gl in glist:
            outf.write(f"{gl}\n")
        for ul in ulist:
            outf.write(f"{ul}\n")

    # delete potential shadow so sysusers does not fail
    (paths.bldroot() / "etc/shadow").unlink(missing_ok=True)

    chroot.enter("sd-sysusers", check=True)
