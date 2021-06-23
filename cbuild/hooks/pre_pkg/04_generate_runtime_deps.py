from cbuild.core import logger, chroot, paths, version

import os
import pathlib
import subprocess

def invoke(pkg):
    if pkg.noverifyrdeps:
        return

    verify_deps = {}
    pkg.so_requires = []
    curelf = pkg.rparent.current_elfs
    curso = {}

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname = finfo

        if soname:
            curso[soname] = pname
        elif fp.suffix == ".so" and str(fp.parent) == "usr/lib":
            curso[soname] = fp.name

        if ("/" + str(fp)) in pkg.skiprdeps:
            pkg.log(f"skipping dependency scan for {str(fp)}")
            continue

        for n in needed:
            verify_deps[n] = True

    broken = False
    log = logger.get()

    # FIXME: also emit dependencies for proper version constraints
    for dep in verify_deps:
        # current package or a subpackage
        if dep in curso:
            depn = curso[dep]
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
