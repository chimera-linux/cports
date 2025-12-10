from cbuild.core import logger, chroot, paths, scanelf
from cbuild.util import flock
from cbuild.apk import cli, util as autil

import re
import os
import pathlib


def _match_skipdep(pkg, f, norel=False):
    if norel:
        rf = f
    else:
        rf = f.relative_to(pkg.destdir)
    for mf in pkg.skip_dependencies:
        if rf.match(mf):
            return None
    return rf


def _scan_so(pkg):
    verify_deps = {}
    pkg.so_requires = []
    curelf = pkg.rparent.current_elfs
    curso = {}
    subpkg_deps = {}
    socache = {}

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname, static, etype, interp, foreign = finfo

        if soname:
            curso[soname] = pname
        elif ".so" in fp.suffixes:
            curso[fp.name] = pname

        if pname != pkg.pkgname:
            continue

        if not _match_skipdep(pkg, fp, True):
            continue

        if foreign:
            continue

        for n in needed:
            verify_deps[n] = True

    broken = False
    log = logger.get()

    # resolve soname: explicit deps first
    for didx in range(len(pkg.depends)):
        dv = pkg.depends[didx]
        dsv = dv.removeprefix("soname:")
        # skip whatever does not match
        if dv == dsv:
            continue
        # strip the provider...
        exc = dsv.find("!")
        if exc > 0:
            prov = dsv[exc:]
            dsv = dsv[0:exc]
        else:
            prov = ""
        # strip version if present
        dvn, dvv, dvop = autil.split_pkg_name(dsv)
        if not dvn:
            # unversioned
            dvn = dsv
        # perform resolution...
        if not dvn.startswith("/"):
            fdvn = f"/usr/lib/{dvn}"
        else:
            fdvn = dvn
        # look up from cache if necessary
        if fdvn in socache:
            soname = socache[fdvn]
        else:
            # pathify
            dvnp = paths.bldroot() / fdvn.removeprefix("/")
            # see if that exists
            if not dvnp.exists():
                log.out(f"  \f[red]SONAME: {dsv} (failed to resolve)")
                broken = True
                continue
            # if so, scan
            sotup = scanelf.scan_one(dvnp)
            if not sotup:
                log.out(f"  \f[red]SONAME: {dsv} (failed to scan)")
                broken = True
                continue
            # extract soname only
            soname = sotup[7]
            socache[fdvn] = soname
        # resolved
        log.out_plain(
            f"  \f[cyan]SONAME: \f[orange]{soname}\f[] <= \f[green]{dsv}\f[] (\f[orange]resolved\f[], \f[green]explicit\f[])"
        )
        if dvv:
            pkg.depends[didx] = f"so:{soname}{dvop}{dvv}{prov}"
        else:
            pkg.depends[didx] = f"so:{soname}{prov}"

    # FIXME: also emit dependencies for proper version constraints
    for dep in verify_deps:
        if dep in pkg.ignore_shlibs:
            log.out_plain(
                f"  \f[cyan]SONAME: \f[orange]{dep}\f[] (\f[orange]ignored\f[], \f[green]explicit\f[])"
            )
            continue
        # current package or a subpackage
        if dep in curso:
            depn = curso[dep]
            if depn == pkg.pkgname:
                # current package: ignore
                log.out_plain(
                    f"  \f[cyan]SONAME: \f[orange]{dep}\f[] (provider: \f[green]{depn}\f[], \f[orange]ignored\f[], same package)"
                )
            else:
                # subpackage: add
                log.out_plain(
                    f"  \f[cyan]SONAME: \f[orange]{dep}\f[] (provider: \f[green]{depn}\f[])"
                )
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
            log.out(f"  \f[red]SONAME: {dep} (unknown provider)")
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
            log.out(f"  \f[red]SONAME: {dep} (unknown provider)")
            broken = True
            continue
        # we found a package
        log.out_plain(
            f"  \f[cyan]SONAME: \f[orange]{dep}\f[] (provider: \f[green]{sdep}\f[])"
        )
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
        if not _match_skipdep(pkg, v):
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
            pkg.error(
                "failed scanning .pc files",
                hint="maybe you need to put 'pkgconf' in 'hostmakedepends'",
            )
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
            # this should never happen in practice since it's already checked
            if not prov:
                pkg.error(f"  pc: {k} (unknown provider)")
            else:
                log.out_plain(
                    f"  \f[cyan]pc: \f[orange]{k}\f[] (provider: \f[green]{prov}\f[])"
                )
            # warn about redundancy
            if prov in pkg.depends:
                pkg.log_warn(f"redundant runtime dependency '{prov}'")
            continue
        # no provider found
        pkg.error(
            f"  pc: {k} (unknown provider)",
            hint=f"add package providing '{k}' to 'makedepends'",
        )


def _scan_svc(pkg):
    svcreq = {}
    log = logger.get()

    def scan_svc(v, pfx):
        if not v.is_file():
            return
        if not _match_skipdep(pkg, v):
            return
        with v.open() as df:
            for ln in df:
                if ln.startswith("#"):
                    continue
                ln = ln.strip()
                eq = ln.find("=")
                cl = ln.find(":")
                if cl > 0 and (eq < 0 or cl < eq):
                    eq = -1
                    key = ln[0:cl].strip()
                    val = ln[cl + 1 :].strip()
                elif eq > 0:
                    cl = -1
                    key = ln[0:eq].strip()
                    val = ln[eq + 1 :].strip()
                else:
                    continue
                match key:
                    case "depends-on" | "depends-ms" | "waits-for":
                        atsig = val.find("@")
                        if atsig > 0:
                            val = val[0:atsig]
                        svcreq[val] = pfx
                    case _:
                        pass

    def pkg_provides_svc(pkg, pn, pfx):
        pth = pkg.destdir / "usr/lib/dinit.d"
        if pfx == "usvc":
            pth = pth / "user"
        if (pth / pn).exists():
            return True
        return False

    def subpkg_provides_svc(pn, pfx):
        for sp in pkg.rparent.subpkg_list:
            if pkg_provides_svc(sp, pn, pfx):
                return sp.pkgname
        return None

    pkg.svc_requires = []

    for f in pkg.destdir.glob("usr/lib/dinit.d/*"):
        scan_svc(f, "svc")

    for f in pkg.destdir.glob("usr/lib/dinit.d/user/*"):
        scan_svc(f, "usvc")

    for sv in svcreq:
        pfx = svcreq[sv]
        # provided by self
        if pkg_provides_svc(pkg, sv, pfx):
            continue
        # provided by one of ours or by a dependency
        in_subpkg = subpkg_provides_svc(sv, pfx)
        if in_subpkg or cli.is_installed(f"{pfx}:" + sv, pkg):
            pkg.svc_requires.append(f"{pfx}:{sv}")
            # locate the explicit provider
            if not in_subpkg:
                prov = cli.get_provider(f"{pfx}:{sv}", pkg)
            else:
                prov = in_subpkg
            if not prov:
                pkg.error(f"  {pfx}: {sv} (unknown provider)")
            else:
                log.out_plain(
                    f"  \f[cyan]{pfx}: \f[orange]{sv}\f[] (provider: \f[green]{prov}\f[])"
                )
            # warn about redundancy
            if prov in pkg.depends and prov != "dinit-chimera":
                pkg.log_warn(f"redundant runtime dependency '{prov}'")
            continue
        # no provider found
        pkg.error(
            f"  {pfx}: {sv} (unknown provider)",
            hint=f"add package providing '{sv}' to 'makedepends'",
        )


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
        # relativize
        ssrc = _match_skipdep(pkg, f)
        if not ssrc:
            continue
        # resolve
        starg = f.readlink()
        # normalize to absolute path within destdir
        if starg.is_absolute():
            sdest = pkg.destdir / starg.relative_to("/")
        else:
            sdest = f.parent / starg
        # if it resolves, it exists within the package, so skip
        if _exists_link(sdest):
            continue
        # otherwise it's a broken symlink, relativize to destdir
        sdest = sdest.relative_to(pkg.destdir)
        # check each subpackage for the file
        for sp in pkg.rparent.subpkg_list:
            np = sp.destdir / sdest
            if _exists_link(np):
                log.out_plain(
                    f"  \f[cyan]symlink: \f[orange]{ssrc}\f[] (points to: \f[orange]{starg}\f[], provider: {sp.pkgname})"
                )
                subpkg_deps[sp.pkgname] = True
                break
        else:
            # could be a main package too
            if _exists_link(pkg.rparent.destdir / sdest):
                log.out_plain(
                    f"  \f[cyan]symlink: \f[orange]{ssrc}\f[] (points to: \f[orange]{starg}\f[], provider: {pkg.rparent.pkgname})"
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
                pkg.error(
                    f"  symlink: {ssrc} (points to: {starg}, unknown provider)",
                    hint="your symlink probably points to a foreign package",
                )

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
        if not pkg.autopkg:
            _scan_so(pkg)
            _scan_pc(pkg)
            _scan_symlinks(pkg)
        _scan_svc(pkg)
