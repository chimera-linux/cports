from cbuild.core import logger


def invoke(pkg):
    if not pkg.options["scancmd"] or pkg.stage == 0:
        return

    cmds = []
    cmdset = {}

    for p in pkg.provides:
        if not p.startswith("cmd:"):
            continue
        cmdname = p[4:]
        versep = cmdname.find("=")
        if versep > 0:
            cmdset[cmdname[:versep]] = True
        else:
            cmdset[cmdname] = True
        logger.get().out_plain(f"   cmd: {cmdname} (explicit)")

    for f in pkg.destdir.glob("usr/bin/*"):
        if f.name in cmdset:
            continue
        # forbidden characters
        if any(v in f.name for v in "[]=<>~"):
            continue
        logger.get().out_plain(f"   cmd: {f.name} from usr/bin")
        if pkg.alternative:
            cmds.append(f.name + "=0")
        else:
            cmds.append(f.name + f"={pkg.pkgver}-r{pkg.pkgrel}")

    cmds.sort()

    if len(cmds) == 0:
        return

    pkg.cmd_provides = cmds
