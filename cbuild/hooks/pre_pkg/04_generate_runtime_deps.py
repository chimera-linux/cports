from cbuild.core import logger, chroot, paths, version

import os
import pathlib
import subprocess

def invoke(pkg):
    if pkg.noverifyrdeps:
        return

    curfilemap = {}
    verify_deps = {}
    pkg.so_requires = []

    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            fp = pathlib.Path(root) / f

            curfilemap[f] = True

            if fp.is_symlink():
                continue

            if not os.access(fp, os.W_OK):
                continue

            with open(fp, "rb") as fh:
                if fh.read(4) != b"\x7FELF":
                    continue

            ff = fp.relative_to(pkg.destdir)

            if "/" + str(ff) in pkg.skiprdeps:
                pkg.log(f"skipping dependency scan for {ff}")
                continue

            for ln in chroot.enter(
                pkg.rparent.tools["OBJDUMP"], [
                    "-p", str(pkg.chroot_destdir / ff)
                ],
                capture_out = True, bootstrapping = pkg.bootstrapping
            ).stdout.splitlines():
                ln = ln.strip()
                if not ln.startswith(b"NEEDED"):
                    continue
                ln = ln[6:].strip().decode("ascii")
                if not ln in verify_deps:
                    verify_deps[ln] = True

    broken = False
    log = logger.get()

    # FIXME: also emit dependencies for proper version constraints
    for dep in verify_deps:
        # current package or a subpackage
        if dep in pkg.rparent.current_sonames:
            depn = pkg.rparent.current_sonames[dep]
            if depn == pkg.pkgname:
                # current package: ignore
                log.out_plain(f"   SONAME: {dep} <-> {depn} (ignored)")
            else:
                # subpackage: add
                log.out_plain(f"   SONAME: {dep} <-> {depn}")
                pkg.so_requires.append(dep)
            continue
        # otherwise, check if it came from an installed dependency
        info = subprocess.run([
            "apk", "info", "--root", str(paths.masterdir()),
            "--installed", "so:" + dep
        ], capture_output = True)
        if info.returncode != 0:
            log.out_red(f"   SONAME: {dep} <-> UNKNOWN PACKAGE!")
            broken = True
            continue
        sdep = info.stdout.strip().decode()
        if len(sdep) == 0:
            # this should never happen though
            log.out_red(f"   SONAME: {dep} <-> UNKNOWN PACKAGE!")
            broken = True
            continue
        # we found a package
        log.out_plain(f"   SONAME: {dep} <-> {sdep}")
        pkg.so_requires.append(dep)

    if broken:
        pkg.error("cannot guess required shlibs")

    # add any explicit deps
    pkg.so_requires += pkg.shlib_requires
