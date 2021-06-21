from cbuild.core import logger, chroot

import os
import pathlib

def _matches_lib(sfxs, root, destdir):
    if len(sfxs) == 0:
        return False

    if len(sfxs) == 1:
        return root == (destdir / "usr/lib")

    sfxs = sfxs[1:]

    for sfx in sfxs:
        try:
            int(sfx[1:])
        except ValueError:
            return False

    return True

def invoke(pkg):
    if pkg.noshlibprovides:
        return

    asonames = []
    cursonames = pkg.rparent.current_sonames

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

            sfxs = ff.suffixes

            # we don't care about anything before the .so
            while len(sfxs) > 0 and sfxs[0] != ".so":
                sfxs = sfxs[1:]
            # no .so
            if len(sfxs) == 0:
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

                if _matches_lib(sfxs, root, pkg.destdir):
                    autosfx = "".join(sfxs)[1:]
                    if len(autosfx) == 0:
                        autosfx = ln[ln.rfind(".so") + 4:]
                    if len(autosfx) == 0:
                        autosfx = "0"

                    asonames.append((ln, autosfx))
                    cursonames[ln] = pkg.pkgname
                    relp = os.path.relpath(root, start = pkg.destdir)
                    logger.get().out_plain(f"   SONAME {ln} from {relp}")

            if not got_soname:
                if _matches_lib(sfxs, root, pkg.destdir):
                    asonames.append((ff.name, "0"))
                    cursonames[ff.name] = pkg.pkgname
                    logger.get().out_plain(f"   SONAME {ff.name} from {relp}")

    pkg.aso_provides = asonames
