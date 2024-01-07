from cbuild.core import logger, chroot, paths
from cbuild.util import flock
from cbuild.apk import cli

import re
import os
import pathlib


def _scan_so(pkg):
    verify_deps = {}
    pkg.so_requires = []
    curelf = pkg.rparent.current_elfs
    curso = {}
    subpkg_deps = {}

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname, static, etype, interp, foreign = finfo

        if soname:
            curso[soname] = pname
        elif ".so" in fp.suffixes:
            curso[fp.name] = pname

        if pname != pkg.pkgname:
            continue

        if foreign:
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
                subpkg_deps[depn] = True
            continue
        # otherwise, check if it came from an installed dependency
        bp = pkg.rparent.profile()
        if bp.cross:
            broot = paths.bldroot() / bp.sysroot.relative_to("/")
            aarch = bp.arch
        else:
            broot = None
            aarch = None

        info = cli.call(
            "info",
            ["--from", "installed", "--description", "so:" + dep],
            None,
            root=broot,
            capture_output=True,
            arch=aarch,
            allow_untrusted=True,
        )
        if info.returncode != 0:
            # when bootstrapping, also check the repository
            if pkg.stage == 0:
                info = cli.call(
                    "info",
                    ["--from", "none", "--description", "so:" + dep],
                    "main",
                    capture_output=True,
                    allow_untrusted=True,
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

    for k in subpkg_deps:
        kv = f"{k}={pkg.rparent.pkgver}-r{pkg.rparent.pkgrel}"
        try:
            # if we have a plain dependency in the list,
            # replace it with a versioned dependency
            pkg.depends[pkg.depends.index(k)] = kv
        except ValueError:
            # if the exact dependency is already present, skip it
            if kv not in pkg.depends:
                pkg.depends.append(kv)

    if broken:
        pkg.error("Failed scanning shlib dependencies")


_pc_ops = {
    "=": True,
    "<": True,
    ">": True,
    "<=": True,
    ">=": True,
}


def _scan_pc(pkg):
    pcreq = {}
    log = logger.get()

    # ugly hack to get around scanning when building pkgconf itself
    if (pkg.destdir / "usr/lib/pkgconfig/libpkgconf.pc").exists():
        return

    # all subpackages must declare their pkg-config path for the scan
    pcpaths = []

    if pkg.rparent.profile().cross:
        sr = pkg.rparent.profile().sysroot
        hsr = paths.bldroot() / sr.relative_to("/")
        if (hsr / "usr/lib/pkgconfig").is_dir():
            pcpaths.append(str(sr / "usr/lib/pkgconfig"))
        if (hsr / "usr/share/pkgconfig").is_dir():
            pcpaths.append(str(sr / "usr/share/pkgconfig"))

    for sp in pkg.rparent.subpkg_list:
        if (sp.destdir / "usr/lib/pkgconfig").is_dir():
            pcpaths.append(str(sp.chroot_destdir / "usr/lib/pkgconfig"))
        if (sp.destdir / "usr/share/pkgconfig").is_dir():
            pcpaths.append(str(sp.chroot_destdir / "usr/share/pkgconfig"))

    if (pkg.rparent.destdir / "usr/lib/pkgconfig").is_dir():
        pcpaths.append(str(pkg.rparent.chroot_destdir / "usr/lib/pkgconfig"))
    if (pkg.rparent.destdir / "usr/share/pkgconfig").is_dir():
        pcpaths.append(str(pkg.rparent.chroot_destdir / "usr/share/pkgconfig"))

    pcpaths = ":".join(pcpaths)

    penv = {
        "PKG_CONFIG_PATH": pcpaths,
    }
    if pkg.rparent.profile().cross:
        penv["PKG_CONFIG_SYSROOT_DIR"] = str(pkg.rparent.profile().sysroot)
        penv["PKG_CONFIG_LIBDIR"] = str(
            pkg.rparent.profile().sysroot / "usr/lib/pkgconfig"
        )

    def scan_pc(v):
        if not v.exists():
            return
        # analyze the .pc file
        pcc = chroot.enter(
            "pkg-config",
            "--print-requires",
            "--print-requires-private",
            v.stem,
            capture_output=True,
            bootstrapping=pkg.stage == 0,
            ro_root=True,
            ro_build=True,
            unshare_all=True,
            env=penv,
        )
        if pcc.returncode != 0:
            pkg.error("failed scanning .pc files (missing pkgconf?)")
        # parse the output
        for ln in pcc.stdout.strip().splitlines():
            ln = ln.strip().decode()
            # turn into an apk-compatible format
            ln = re.sub(r"\s*([<>=]+)\s*", r"\1", ln)
            # find where the version constraint begins
            idx = re.search(r"[<>=]+", ln)
            if idx:
                pname = ln[: idx.start()]
                # validate so we don't fail at apk creation stage
                if ln[idx.start() : idx.end()] not in _pc_ops:
                    pkg.error(f"invalid operator in constraint '{ln}'")
                if not cli.check_version(ln[idx.end() :]):
                    pkg.error(f"invalid version in constraint '{ln}'")
            else:
                pname = ln
            # if self-provided, skip
            if (pkg.destdir / f"usr/lib/pkgconfig/{pname}.pc").exists():
                continue
            elif (pkg.destdir / f"usr/share/pkgconfig/{pname}.pc").exists():
                continue
            # external, so depend on it
            pcreq[ln] = pname

    for f in pkg.destdir.glob("usr/lib/pkgconfig/*.pc"):
        scan_pc(f)

    for f in pkg.destdir.glob("usr/share/pkgconfig/*.pc"):
        scan_pc(f)

    pkg.pc_requires = []

    def subpkg_provides_pc(pn):
        for sp in pkg.rparent.subpkg_list:
            if (sp.destdir / f"usr/lib/pkgconfig/{pn}.pc").exists():
                return sp.pkgname
            if (sp.destdir / f"usr/share/pkgconfig/{pn}.pc").exists():
                return sp.pkgname
        return None

    for k in pcreq:
        pn = pcreq[k]
        # provided by one of ours or by a dependency
        in_subpkg = subpkg_provides_pc(pn)
        if in_subpkg or cli.is_installed("pc:" + k, pkg):
            pkg.pc_requires.append(k)
            # locate the explicit provider
            if not in_subpkg:
                # apk search needs unconstrained name
                idx = re.search(r"[<>=]", k)
                if idx:
                    prov = cli.get_provider("pc:" + k[: idx.start()], pkg)
                else:
                    prov = cli.get_provider("pc:" + k, pkg)
            else:
                prov = in_subpkg
            # this should never happen
            if not prov:
                pkg.error(f"   pc: {k} <-> UNKNOWN PACKAGE!")
            else:
                log.out_plain(f"   pc: {k} <-> {prov}")
            # warn about redundancy
            if prov in pkg.depends:
                pkg.log_warn(f"redundant runtime dependency '{prov}'")
            continue
        # no provider found
        pkg.error(f"   pc: {k} <-> UNKNOWN PACKAGE!")


def _scan_symlinks(pkg):
    brokenlinks = pkg.options["brokenlinks"]
    log = logger.get()

    subpkg_deps = {}

    # we use this instead of exists() as exists() will resolve
    # symbolic links, while we're ok with a symlink pointing to
    # a symlink (this is not considered broken, as the other
    # symlink will be checked separately)
    def _exists_link(p):
        try:
            os.lstat(os.path.normpath(p))
        except FileNotFoundError:
            return False
        return True

    for f in pkg.destdir.rglob("*"):
        # skip non-symlinks
        if not f.is_symlink():
            continue
        # resolve
        sdest = f.readlink()
        # normalize to absolute path within destdir
        if sdest.is_absolute():
            sdest = pkg.destdir / sdest.relative_to("/")
        else:
            sdest = f.parent / sdest
        # if it resolves, it exists within the package, so skip
        if _exists_link(sdest):
            continue
        # otherwise it's a broken symlink, relativize to destdir
        sdest = sdest.relative_to(pkg.destdir)
        ssrc = f.relative_to(pkg.destdir)
        # check each subpackage for the file
        for sp in pkg.rparent.subpkg_list:
            np = sp.destdir / sdest
            if _exists_link(np):
                log.out_plain(f"   symlink: {ssrc} -> {sdest} <-> {sp.pkgname}")
                subpkg_deps[sp.pkgname] = True
                break
        else:
            # could be a main package too
            if _exists_link(pkg.rparent.destdir / sdest):
                log.out_plain(
                    f"   symlink: {ssrc} -> {sdest} <-> {pkg.rparent.pkgname}"
                )
                subpkg_deps[pkg.rparent.pkgname] = True
            else:
                # nothing found
                if brokenlinks:
                    continue
                allow_brokenlink = True
                for f in pkg.broken_symlinks:
                    if ssrc.match(f):
                        break
                else:
                    allow_brokenlink = False
                # fine-grained
                if allow_brokenlink:
                    continue
                pkg.error(f"   symlink: {ssrc} -> {sdest} <-> UNKNOWN PACKAGE!")

    for k in subpkg_deps:
        kv = f"{k}={pkg.rparent.pkgver}-r{pkg.rparent.pkgrel}"
        try:
            # if we have a plain dependency in the list,
            # replace it with a versioned dependency
            pkg.depends[pkg.depends.index(k)] = kv
        except ValueError:
            # if the exact dependency is already present, skip it
            if kv not in pkg.depends:
                pkg.depends.append(kv)


def invoke(pkg):
    if not pkg.options["scanrundeps"]:
        return

    with flock.lock(flock.apklock(pkg.rparent.profile().arch)):
        _scan_so(pkg)
        _scan_pc(pkg)
        _scan_symlinks(pkg)
