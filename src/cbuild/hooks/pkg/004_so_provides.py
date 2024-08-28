from cbuild.core import logger
from cbuild.apk import cli

import re
import pathlib


def _matches_lib(soname, root):
    # no soname: drop from earch
    if not soname:
        return False

    # versioned or unversioned soname
    if re.match(r"^\w+(.*)+\.so(\.\d+)*$", soname):
        # versioned soname: match anywhere
        if re.search(r"\d+$", soname):
            return True

        # unversioned soname: only if in libdir
        return str(root) == "usr/lib"


def invoke(pkg):
    if not pkg.options["scanshlibs"] or pkg.autopkg:
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
        sfx = soname[eq + 1 :]
        soname = soname[:eq]
        soset[soname] = True
        logger.get().out_plain(
            f"  \f[cyan]SONAME: \f[orange]{soname}={sfx} \f[green](explicit)\f[]"
        )

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname, static, etype, interp, foreign = finfo

        # we only care about our own
        if pname != pkg.pkgname:
            continue

        # foreign-machine elfs are not scanned
        if foreign:
            continue

        sfxs = fp.suffixes

        # we don't care about anything before the .so
        while len(sfxs) > 0 and sfxs[0] != ".so":
            sfxs = sfxs[1:]

        if _matches_lib(soname, fp.parent):
            autosfx = "".join(sfxs[1:])[1:]
            if len(autosfx) == 0:
                autosfx = "0"
            elif not cli.check_version(autosfx):
                pkg.error(f"invalid so version {autosfx}")

            if soname not in soset:
                asonames.append(
                    (soname, autosfx if not pkg.alternative else "0")
                )
                logger.get().out_plain(
                    f"  \f[cyan]SONAME: \f[orange]{soname}\f[] from \f[green]{fp.parent}\f[]"
                )
            else:
                logger.get().out_plain(
                    f"  \f[cyan]SONAME: \f[orange]{soname}\f[] from \f[green]{fp.parent} \f[orange](skipped)\f[]"
                )

    pkg.aso_provides = asonames
