from cbuild.core import logger, chroot

import os
import re

def invoke(pkg):
    if pkg.noshlibprovides:
        return

    pattern = r"\w+(.*)+\.so(\.[0-9]+)*$"
    vpattern = r"\w+(.*)+\.so(\.[0-9]+)+$"
    sonames = []

    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            fp = os.path.join(root, f)

            if not os.access(fp, os.W_OK):
                continue

            with open(fp, "rb") as fh:
                if fh.read(4) != b"\x7FELF":
                    continue

            ff = os.path.relpath(fp, pkg.destdir)

            for ln in chroot.enter(pkg.rparent.tools["OBJDUMP"], [
                "-p", os.path.join(pkg.chroot_destdir, ff)
            ], capture_out = True).stdout.splitlines():
                ln = ln.strip()
                if not ln.startswith(b"SONAME"):
                    continue
                ln = ln[6:].strip().decode("ascii")

                if re.match(vpattern, ln) or (
                    re.match(pattern, ln) and root == pkg.destdir / "usr/lib"
                ):
                    sonames.append(ln)
                    relp = os.path.relpath(root, start = pkg.destdir)
                    logger.get().out_plain(f"   SONAME {ln} from {relp}")

    sonames += pkg.shlib_provides

    with open(pkg.destdir / "shlib-provides", "w") as f:
        f.write(" ".join(sonames))
