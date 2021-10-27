from cbuild.core import logger, chroot

import os
import pathlib

def _matches_lib(sfxs, root):
    # no .so
    if len(sfxs) == 0:
        return False

    if len(sfxs) == 1:
        return str(root) == "usr/lib"

    sfxs = sfxs[1:]

    for sfx in sfxs:
        try:
            int(sfx[1:])
        except ValueError:
            return False

    return True

def invoke(pkg):
    if not pkg.options["scanshlibs"]:
        return

    asonames = []
    curelf = pkg.rparent.current_elfs

    soset = {}

    # add explicit provides
    for p in pkg.provides:
        if not p.startswith("so:"):
            continue
        soname = p[3:]
        eq = soname.find("=")
        if eq < 0:
            pkg.error(f"invalid explicit shlib: {soname}")
        soname = soname[:eq]
        sfx = soname[eq + 1:]
        soset[soname] = True
        logger.get().out_plain(f"   SONAME {soname}={sfx} (explicit)")

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname, static, etype, interp = finfo

        # we only care about our own
        if pname != pkg.pkgname:
            continue

        sfxs = fp.suffixes

        # we don't care about anything before the .so
        while len(sfxs) > 0 and sfxs[0] != ".so":
            sfxs = sfxs[1:]

        if _matches_lib(sfxs, fp.parent):
            if not soname:
                soname = fp.name
                autosfx = "0"
            else:
                autosfx = "".join(sfxs[1:])[1:]
                if len(autosfx) == 0:
                    autosfx = soname[soname.rfind(".so") + 4:]
                if len(autosfx) == 0:
                    autosfx = "0"

            if not soname in soset:
                asonames.append((soname, autosfx))
                logger.get().out_plain(f"   SONAME {soname} from {fp.parent}")
            else:
                logger.get().out_plain(
                    f"   SONAME {soname} from {fp.parent} (skipped)"
                )

    pkg.aso_provides = asonames
