from cbuild.core import chroot, logger
from cbuild.apk import cli

import re

def invoke(pkg):
    if not pkg.options["scancmd"] or pkg.bootstrapping:
        return

    cmds = []
    cmdset = {}

    for p in pkg.provides:
        if not p.startswith("cmd:"):
            continue
        cmdname = p[4:]
        cmdset[cmdname] = True
        logger.get().out_plain(f"   cmd: {cmdname} (explicit)")

    for f in pkg.destdir.glob("usr/bin/*"):
        if f.name in cmdset:
            continue
        logger.get().out_plain(f"   cmd: {f.name} from usr/bin")
        cmds.append(f.name)

    cmds.sort()

    if len(cmds) == 0:
        return

    pkg.cmd_provides = cmds
