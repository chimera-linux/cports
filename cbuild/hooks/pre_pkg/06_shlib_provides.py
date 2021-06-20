from cbuild.core import logger, chroot

import os
import re
import pathlib

def invoke(pkg):
    if pkg.noshlibprovides:
        return

    pattern = r"\w+(.*)+\.so(\.[0-9]+)*$"
    vpattern = r"\w+(.*)+\.so(\.[0-9]+)+$"
    sonames = []
    asonames = []

    for root, dirs, files in os.walk(pkg.destdir):
        root = pathlib.Path(root)
        for f in files:
            fp = root / f

            if not os.access(fp, os.W_OK):
                continue

            if fp.is_symlink():
                continue

            with open(fp, "rb") as fh:
                if fh.read(4) != b"\x7FELF":
                    continue

            ff = fp.relative_to(pkg.destdir)

            if len(ff.suffixes) == 0 or ff.suffixes[0] != ".so":
                continue

            got_soname = False
            for ln in chroot.enter(
                pkg.rparent.tools["OBJDUMP"], [
                    "-p", str(pkg.chroot_destdir / ff)
                ],
                capture_out = True, bootstrapping = pkg.bootstrapping
            ).stdout.splitlines():
                ln = ln.strip()
                if not ln.startswith(b"SONAME"):
                    continue
                ln = ln[6:].strip().decode("ascii")
                got_soname = True

                if re.match(vpattern, ln) or (
                    re.match(pattern, ln) and root == pkg.destdir / "usr/lib"
                ):
                    sonames.append(ln)
                    autosfx = "".join(ff.suffixes[1:])[1:]
                    if len(autosfx) == 0:
                        autosfx = ln[ln.rfind(".so") + 4:]
                    if len(autosfx) == 0:
                        autosfx = "0"
                    asonames.append((ln, autosfx))
                    relp = os.path.relpath(root, start = pkg.destdir)
                    logger.get().out_plain(f"   SONAME {ln} from {relp}")

            if not got_soname:
                if re.match(vpattern, ff.name) or (
                    re.match(pattern, ff.name) and root == pkg.destdir / "usr/lib"
                ):
                    asonames.append((ff.name, "0"))

    sonames += pkg.shlib_provides
    pkg.aso_provides = asonames
    pkg.so_provides = sonames
