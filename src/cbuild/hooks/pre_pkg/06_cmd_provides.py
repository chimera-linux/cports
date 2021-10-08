from cbuild.core import chroot
from cbuild.apk import cli

import re

def invoke(pkg):
    if not pkg.options["scancmd"] or pkg.bootstrapping:
        return

    cmds = []

    for f in pkg.destdir.glob("usr/bin/*"):
        cmds.append(f.name)

    cmds.sort()

    if len(cmds) == 0:
        return

    pkg.cmd_provides = cmds
