# prepares /etc/passwd and /etc/group as needed to generate packages

from cbuild.core import paths


def invoke(pkg):
    # don't involve users during bootstrap
    if pkg.stage < 1:
        return

    # group ids of individual groups go down
    startgid = 999
    # user/pgroup ids go up, and are higher than cbuild
    # cbuild user is 1337, we should never go this high
    # if we for some reason do, it acts as a sentinel
    startuid = 1000

    groupset = {}
    userset = {}
    glist = []
    ulist = []

    # first get the groups we have
    with open(paths.bldroot() / "etc/group") as grf:
        for grl in grf:
            grl = grl.strip()
            grpn, grpw, gid, gmemb = grl.split(":")
            groupset[grpn] = int(gid)
            groupset[int(gid)] = grpn
            glist.append(grl)

    # then the users we have
    with open(paths.bldroot() / "etc/passwd") as usf:
        for usl in usf:
            usl = usl.strip()
            usrn, uspw, uid, gid, ucmt, uhm, ush = usl.split(":")
            userset[usrn] = int(uid)
            userset[int(uid)] = usrn
            ulist.append(usl)

    # adjust the start ids according to existing stuff
    while startuid in userset:
        startuid += 1
    while startgid in groupset:
        startgid -= 1

    ulen = len(ulist)
    glen = len(glist)

    # add new groups
    for g in pkg.system_groups:
        gl = g.split(":")
        if len(gl) == 1:
            gname = g
            gid = startgid
            startgid -= 1
        else:
            gname = gl[0]
            gid = int(gl[1])
        # validate
        if gname in groupset:
            pkg.error(f"group '{gname}' already registered")
        if gid in groupset:
            pkg.error(f"gid '{gid}' already used by '{groupset[gid]}'")
        # now add
        groupset[gname] = gid
        groupset[gid] = gname
        glist.append(f"{gname}:x:{gid}:")

    # add new users
    for u in pkg.system_users:
        checkgrp = True
        if isinstance(u, dict):
            uname = u["name"]
            uid = u["id"]
            if not uid:
                uid = startuid
                startuid += 1
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
                if gn not in groupset:
                    pkg.error(f"invalid primary group '{gn}' for '{uname}'")
                gid = groupset[gn]
                checkgrp = False
            else:
                gid = uid
        else:
            ul = u.split(":")
            if len(ul) == 1:
                uname = u
                uid = startuid
            else:
                uname = ul[0]
                uid = int(ul[1])
            # remaining info is automatic
            gid = uid
            startuid += 1
            uhm = "/tmp"
            ucmt = f"{uname} user"
            ush = "/bin/sh"
        # validate that we can add this new group
        if checkgrp:
            if gid in groupset:
                pkg.error(f"gid {gid} belongs to '{groupset[gid]}'")
            if uname in groupset:
                pkg.error(f"group name '{uname}' already exists")
            # add to groups
            groupset[uname] = uid
            groupset[uid] = uname
            glist.append(f"{uname}:x:{uid}:")
        # validate that this user can be added
        if uname in userset:
            pkg.error(f"user '{uname}' already registered")
        if uid in userset:
            pkg.error(f"uid '{uid}' already used by '{userset[uid]}'")
        # finally add
        ulist.append(f"{uname}:x:{uid}:{gid}:{ucmt}:{uhm}:{ush}")

    # new groups were added, rewrite group
    if len(glist) > glen:
        with open(paths.bldroot() / "etc/group", "w") as grf:
            for gl in glist:
                grf.write(gl)
                grf.write("\n")

    # new users were added, rewrite passwd
    if len(ulist) > ulen:
        with open(paths.bldroot() / "etc/passwd", "w") as usf:
            for ul in ulist:
                usf.write(ul)
                usf.write("\n")
