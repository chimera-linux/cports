from cbuild.core import logger, chroot, paths, version
from cbuild.apk import cli

import os
import pathlib
import subprocess

def invoke(pkg):
    if not pkg.options["scanrundeps"]:
        return

    verify_deps = {}
    pkg.so_requires = []
    curelf = pkg.rparent.current_elfs
    curso = {}

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname, static = finfo

        if soname:
            curso[soname] = pname
        elif fp.suffix == ".so" and str(fp.parent) == "usr/lib":
            curso[fp.name] = pname

        if pname != pkg.pkgname:
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
        bp = pkg.rparent.build_profile
        if bp.cross:
            broot = paths.bldroot() / bp.sysroot.relative_to("/")
            aarch = bp.arch
        else:
            broot = None
            aarch = None

        info = cli.call(
            "info", ["--installed", "--description", "so:" + dep], None,
            root = broot, capture_output = True, arch = aarch,
            allow_untrusted = True
        )
        if info.returncode != 0:
            # when bootstrapping, also check the repository
            if pkg.bootstrapping:
                info = cli.call(
                    "info", ["--description", "so:" + dep], "main",
                    capture_output = True, allow_untrusted = True
                )

        # either of the commands failed
        if info.returncode != 0:
            log.out_red(f"   SONAME: {dep} <-> UNKNOWN PACKAGE!")
            broken = True
            continue

        # this needs a bit more parsing, first take only the name-ver
        outl = info.stdout.split()
        sdep = None
        if len(outl) > 0:
            outl = outl[0].strip().decode()
            # find -rX
            dash = outl.rfind("-")
            if dash > 0:
                # find the version separator
                dash = outl.rfind("-", 0, dash)
                if dash > 0:
                    # consider just the name
                    sdep = outl[0:dash]

        if not sdep or len(sdep) == 0:
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
