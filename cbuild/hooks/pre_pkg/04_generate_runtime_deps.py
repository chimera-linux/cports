from cbuild.core import logger, chroot, paths, xbps, version

import os
import pathlib

def add_rundep(pkg, sdep):
    depn = xbps.get_pkg_dep_name(sdep)
    if not depn:
        depn = xbps.get_pkg_name(sdep)

    found = False

    for dep in pkg.run_depends:
        rdepn = xbps.get_pkg_dep_name(dep)
        if not rdepn:
            rdepn = xbps.get_pkg_name(dep)

        if rdepn != depn:
            continue

        if version.compare(rdepn, depn) < 0:
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
            dn = xbps.get_pkg_dep_name(d)
            pn = xbps.get_pkg_name(d)
            if not dn and not pn:
                d += ">=0"
            dl.append(d)
        with open(pkg.destdir / "rdeps", "w") as rdeps:
            rdeps.write(" ".join(dl))

def invoke(pkg):
    shlibmap = paths.cbuild() / "shlibs"

    if pkg.noverifyrdeps:
        store_rundeps(pkg)
        return

    curfilemap = {}
    verify_deps = {}
    pkg.so_requires = []

    for root, dirs, files in os.walk(pkg.destdir):
        for f in files:
            fp = pathlib.Path(root) / f

            curfilemap[f] = True

            if not os.access(fp, os.W_OK):
                continue

            with open(fp, "rb") as fh:
                if fh.read(4) != b"\x7FELF":
                    continue

            ff = fp.relative_to(pkg.destdir)

            if "/" + str(ff) in pkg.skiprdeps:
                pkg.log(f"skipping dependency scan for {ff}")
                continue

            for ln in chroot.enter(pkg.rparent.tools["OBJDUMP"], [
                "-p", str(pkg.chroot_destdir / ff)
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
                pkgn = xbps.get_pkg_name(d)
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

        pkgn = xbps.get_pkg_name(rdep)
        pkgv = xbps.get_pkg_version(rdep)

        if not pkgn or len(pkgv) == 0:
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

    if broken:
        pkg.error("cannot guess required shlibs")

    store_rundeps(pkg)

    # add any explicit deps
    pkg.so_requires += pkg.shlib_requires
