from cbuild.core import logger, chroot, paths, xbps

import os
import pathlib

def add_rundep(pkg, sdep):
    depn = chroot.invoke_xcmd(xbps.uhelper(), [
        "getpkgdepname", sdep
    ]).stdout.strip().decode("ascii")

    if len(depn) == 0:
        depn = chroot.invoke_xcmd(xbps.uhelper(), [
            "getpkgname", sdep
        ]).stdout.strip().decode("ascii")

    found = False

    for dep in pkg.run_depends:
        rdepn = chroot.invoke_xcmd(xbps.uhelper(), [
            "getpkgdepname", dep
        ]).stdout.strip().decode("ascii")

        if len(rdepn) == 0:
            rdepn = chroot.invoke_xcmd(xbps.uhelper(), [
                "getpkgname", dep
            ]).stdout.strip().decode("ascii")

        if rdepn != depn:
            continue

        if chroot.invoke_xcmd(xbps.uhelper(), [
            "cmpver", dep, sdep
        ]).returncode == 255:
            for n, v in enumerate(pkg.run_depends):
                if v == dep:
                    pkg.run_depends[n] = sdep
        found = True

    if not found:
        pkg.run_depends.append(sdep)

def store_rundeps(pkg):
    if len(pkg.run_depends) > 0:
        dl = []
        for d in pkg.run_depends:
            dn = chroot.invoke_xcmd(xbps.uhelper(), [
                "getpkgdepname", d
            ]).stdout.strip()
            pn = chroot.invoke_xcmd(xbps.uhelper(), [
                "getpkgname", d
            ]).stdout.strip()
            if len(dn) == 0 and len(pn) == 0:
                d += ">=0"
            dl.append(d)
        with open(pkg.destdir / "rdeps", "w") as rdeps:
            rdeps.write(" ".join(dl))

def invoke(pkg):
    shlibmap = os.path.join(paths.cbuild(), "shlibs")

    if pkg.noverifyrdeps:
        store_rundeps(pkg)
        return

    curfilemap = {}
    verify_deps = {}
    pkg.so_requires = []

    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            fp = os.path.join(root, f)

            curfilemap[f] = True

            if not os.access(fp, os.W_OK):
                continue

            with open(fp, "rb") as fh:
                if fh.read(4) != b"\x7FELF":
                    continue

            ff = os.path.relpath(fp, pkg.destdir)

            if ff in pkg.skiprdeps:
                pkg.log(f"skipping dependency scan for {ff}")
                continue

            for ln in chroot.enter(pkg.rparent.tools["OBJDUMP"], [
                "-p", os.path.join(pkg.chroot_destdir, ff)
            ], capture_out = True).stdout.splitlines():
                ln = ln.strip()
                if not ln.startswith(b"NEEDED"):
                    continue
                ln = ln[6:].strip().decode("ascii")
                if not ln in verify_deps:
                    verify_deps[ln] = True

    shmap = {}
    with open(shlibmap) as f:
        for ln in f:
            ln = ln.strip()
            if ln.startswith("#"):
                continue

            sv = ln.split()
            solib, pkgn = sv[0], sv[1]
            if not solib in shmap:
                shl = []
                shmap[solib] = shl
            else:
                shl = shmap[solib]

            shmap[solib].append(pkgn)

    broken = False
    log = logger.get()

    for dep in verify_deps:
        # dependency not in shlibs
        if not dep in shmap:
            # dependency not in current pkg
            if not dep in curfilemap:
                log.out_red(f"   SONAME: {dep} <-> UNKNOWN PKG PLEASE FIX!")
                broken = True
            else:
                log.out_plain(f"   SONAME: {dep} <-> {pkg.name} (ignored)")
            continue
        elif len(shmap[dep]) > 1:
            # check if provided by multiple packages
            rdep = None
            for d in shmap[dep]:
                pkgn = chroot.invoke_xcmd(xbps.uhelper(), [
                    "getpkgname", d
                ]).stdout.strip().decode("ascii")
                if pkgn == pkg.rparent.pkgname:
                    rdep = d
                    break
                else:
                    # assume we found something for now
                    found = True
                    for sp in pkg.rparent.subpkg_list:
                        if pkgn == sp.pkgname:
                            rdep = d
                            break
                    else:
                        # called when no break was encountered
                        found = False
                    if found:
                        break
        else:
            rdep = shmap[dep][0]

        pkgn = chroot.invoke_xcmd(xbps.uhelper(), [
            "getpkgname", rdep
        ]).stdout.strip().decode("ascii")
        pkgv = chroot.invoke_xcmd(xbps.uhelper(), [
            "getpkgversion", rdep
        ]).stdout.strip().decode("ascii")

        if len(pkgn) == 0 or len(pkgv) == 0:
            log.out_red(f"   SONAME: {dep} <-> UNKNOWN PKG PLEASE FIX!")
            broken = True
            continue

        sdep = f"{pkgn}>={pkgv}"
        for sp in pkg.rparent.subpkg_list:
            if sp == pkgn:
                sdep = f"{pkgn}-{pkg.version}_{pkg.revision}"
                break

        if pkgn != pkg.pkgname:
            log.out_plain(f"   SONAME: {dep} <-> {sdep}")
            pkg.so_requires.append(dep)
        else:
            # ignore libs by current package
            log.out_plain(f"   SONAME: {dep} <-> {rdep} (ignored)")
            continue

        add_rundep(pkg, sdep)

    store_rundeps(pkg)

    # add any explicit deps
    pkg.so_requires += pkg.shlib_requires
