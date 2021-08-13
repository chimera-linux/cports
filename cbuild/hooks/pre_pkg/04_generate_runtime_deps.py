from cbuild.core import logger, chroot, paths, version
from cbuild.apk import cli

import os
import pathlib
import subprocess

# a special map since these are used from the host during bootstrap stage
bootstrap_map = {
    "libc.so": "musl",
    "libc++.so.1": "libcxx",
    "libunwind.so.1": "libunwind",
}

def invoke(pkg):
    if not pkg.options["scanrdeps"]:
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

        if ("/" + str(fp)) in pkg.skiprdeps:
            pkg.log(f"skipping dependency scan for {fp}")
            continue

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
        if not pkg.bootstrapping or not (dep in bootstrap_map):
            aopts = ["--allow-untrusted", "--installed"]
            bp = pkg.rparent.build_profile
            if bp.cross:
                broot = paths.masterdir() / bp.sysroot.relative_to("/")
                aopts += ["--arch", bp.arch]
            else:
                broot = None
            aopts += ["so:" + dep]
            info = cli.call(
                "info", aopts, None, capture_output = True, root = broot
            )
            if info.returncode != 0:
                log.out_red(f"   SONAME: {dep} <-> UNKNOWN PACKAGE!")
                broken = True
                continue
            sdep = info.stdout.strip().decode()
        else:
            sdep = bootstrap_map[dep]
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
