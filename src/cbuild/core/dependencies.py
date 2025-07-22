from cbuild.core import logger, template, paths, chroot
from cbuild.apk import util as autil, cli as apki
from cbuild.util import flock

# avoid re-parsing same templates every time; the pkgver will
# never be conditional and that is the only thing we care about
_tcache = {}


def _srcpkg_ver(pkgn, pkgb):
    if pkgn in _tcache:
        return _tcache[pkgn]

    tmplpath = None
    for r in pkgb.source_repositories:
        tmplpath = paths.distdir() / r / pkgn / "template.py"
        if tmplpath.is_file():
            break
        else:
            tmplpath = None

    if not tmplpath:
        altname = None
        for apkg, adesc, iif, takef in template.autopkgs:
            if pkgn.endswith(f"-{apkg}"):
                altname = pkgn.removesuffix(f"-{apkg}")
                break
        if altname:
            for r in pkgb.source_repositories:
                rpath = paths.distdir() / r
                tmplpath = rpath / altname / "template.py"
                if tmplpath.is_file():
                    break
                else:
                    tmplpath = None

    if not tmplpath:
        return None, None

    pkgp = tmplpath.resolve().parent

    tmplv = template.Template(
        pkgp,
        pkgb.profile().arch,
        True,
        False,
        (1, 1),
        False,
        False,
        None,
        init=False,
    )

    modv = tmplv._raw_mod
    if not hasattr(modv, "pkgver") or not hasattr(modv, "pkgrel"):
        return None, tmplv.full_pkgname

    pver = getattr(modv, "pkgver")
    prel = getattr(modv, "pkgrel")
    if pver is None or prel is None:
        return None, tmplv.full_pkgname

    cv = f"{pver}-r{prel}"
    _tcache[pkgn] = (cv, tmplv.full_pkgname)

    return cv, tmplv.full_pkgname


def _is_rdep(pn):
    if pn.startswith("so:"):
        return False
    elif pn.startswith("pc:"):
        return False
    elif pn.startswith("cmd:"):
        return False
    elif pn.startswith("alt:"):
        return False
    elif pn.startswith("virtual:"):
        return False

    return True


def setup_depends(pkg, only_names=False):
    hdeps = []
    tdeps = []
    rdeps = []

    pkg.resolve_depends()

    crdeps = [(pkg.pkgname, x) for x in pkg.depends]

    # also account for subpackages
    for sp in pkg.subpkg_list:
        for x in sp.depends:
            crdeps.append((sp.pkgname, x))

    for orig, dep in crdeps:
        # conflicts are not checked at all
        if dep.startswith("!"):
            continue

        pn, pv, pop = autil.split_pkg_name(dep)

        # virtual dependencies are checked for their specified provider
        if not _is_rdep(dep):
            # locate the provider
            ppos = dep.find("!")
            if ppos < 0:
                pkg.error(
                    f"virtual dependency '{dep}' has no specified provider",
                    hint="specify one by appending '!provider'",
                )
            # alternatives need special resolution
            if dep.startswith("alt:"):
                dep = f"{dep[4:ppos]}-{dep[ppos + 1 :]}-default"
            else:
                dep = dep[ppos + 1 :]
            pn, pv, pop = autil.split_pkg_name(dep)

        if only_names:
            if pn:
                rdeps.append((orig, pn))
            else:
                rdeps.append((orig, dep))
        elif not pn:
            rdeps.append((orig, dep + ">=0"))
        else:
            rdeps.append((orig, dep))

    cdeps = []
    if not pkg.profile().cross and (pkg.options["check"] or pkg._force_check):
        cdeps = pkg.checkdepends

    if pkg.stage > 0 and not only_names:
        for dep in pkg.hostmakedepends + cdeps:
            sver, sfull = _srcpkg_ver(dep, pkg)
            if not sver:
                hdeps.append((None, dep, sfull))
                continue
            hdeps.append((sver, dep, sfull))
    elif only_names:
        hdeps = pkg.hostmakedepends + cdeps

    if not only_names:
        for dep in pkg.makedepends:
            sver, sfull = _srcpkg_ver(dep, pkg)
            if not sver:
                tdeps.append((None, dep, sfull))
                continue
            tdeps.append((sver, dep, sfull))
    else:
        tdeps = pkg.makedepends

    return hdeps, tdeps, rdeps


def _install_from_repo(pkg, pkglist, cross=False):
    from cbuild.apk import sign

    signkey = sign.get_keypath()

    if pkg.stage == 0:
        ret = apki.call(
            "add",
            ["--usermode", "--no-scripts", *pkglist],
            pkg,
            capture_output=True,
            allow_untrusted=not signkey,
        )
    elif cross and pkg.profile().cross:
        ret = apki.call_chroot(
            "add",
            [
                "--root",
                str(pkg.profile().sysroot),
                "--no-scripts",
                *pkglist,
            ],
            pkg,
            capture_output=True,
            arch=pkg.profile().arch,
            allow_untrusted=not signkey,
        )
    else:
        # write world file and fix instead of adding to account for previous
        # world being potentially dirty and having a different package set
        with open(paths.bldroot() / "etc/apk/world", "w") as wf:
            for pkgn in chroot.get_world_base():
                wf.write(f"{pkgn}\n")
            for pkgn in pkglist:
                wf.write(f"{pkgn}\n")
        # and then perform the transaction
        ret = apki.call_chroot(
            "fix",
            [],
            pkg,
            capture_output=True,
            allow_untrusted=not signkey,
        )
    if ret.returncode != 0:
        outl = ret.stderr.strip().decode()
        outx = ret.stdout.strip().decode()
        if len(outl) > 0:
            pkg.logger.out_plain(">> stderr:")
            pkg.logger.out_plain(outl)
        if len(outx) > 0:
            pkg.logger.out_plain(">> stdout:")
            pkg.logger.out_plain(outx)
        pkg.error("failed to install dependencies")


def _get_vers(pkgs, pkg, sysp, arch):
    plist = list(pkgs)
    if len(plist) == 0:
        return {}, None

    ret = {}
    with flock.lock(flock.apklock(arch if arch else chroot.host_cpu())):
        out, crepos = apki.call(
            "search",
            ["--from", "none", "-e", "-a", *plist],
            pkg,
            root=sysp,
            capture_output=True,
            arch=arch,
            allow_untrusted=True,
            return_repos=True,
        )
    if out.returncode != 0:
        return None, None

    # map the output to a dict
    for f in out.stdout.strip().decode().split("\n"):
        nn, nv = autil.get_namever(f)
        if nn not in ret:
            ret[nn] = [nv]
        else:
            ret[nn].append(nv)

    return ret, crepos


def _is_available(pkgn, pkgop, pkgv, pkg, vers, crepos, sysp, arch):
    if pkgn not in vers:
        return None

    pvers = vers[pkgn]

    # we don't care about ver so take latest (it's what apk would install)
    if not pkgv:
        return pvers[-1]

    ppat = pkgn + pkgop + pkgv

    # first match against every version available
    for apn in reversed(pvers):
        # matched at least one version
        if autil.pkg_match(f"{pkgn}-{apn}", ppat):
            break
    else:
        # matched no version, so build
        return None

    # only one version, so it's unambiguous
    if len(pvers) == 1:
        return pvers[0]

    # now check repos individually in priority order
    with flock.lock(flock.apklock(arch)):
        for cr in crepos:
            if cr == "--repository":
                continue
            st = (
                apki.call(
                    "search",
                    ["--from", "none", "--repository", cr, "-e", "-a", pkgn],
                    None,
                    root=sysp,
                    capture_output=True,
                    arch=arch,
                    allow_untrusted=True,
                )
                .stdout.strip()
                .decode()
            )
            if len(st) == 0:
                continue
            pn = st.split("\n")
            # highest priority repo takes all
            if len(pn) > 0:
                if autil.pkg_match(pn[0], ppat):
                    nn, nv = autil.get_namever(pn[0])
                    return nv
                return None

    # no match in individual repos? this should be unreachable
    return None


def install(pkg, origpkg, step, depmap, hostdep, update_check):
    style = ""
    if pkg.build_style:
        style = f" [{pkg.build_style}]"

    pprof = pkg.profile()
    tarch = pprof.arch
    cross = not not pprof.cross

    if pkg.pkgname != origpkg:
        pkg.log(f"building{style} (dependency of {origpkg}) for {tarch}...")
    else:
        pkg.log(f"building{style} for {tarch}...")

    host_binpkg_deps = []
    binpkg_deps = []
    host_missing_deps = []
    missing_deps = []

    log = logger.get()

    ihdeps, itdeps, irdeps = setup_depends(pkg)

    # ensure cross-toolchain is included in hostdeps
    if cross:
        sver, sfull = _srcpkg_ver(f"base-cross-{pprof.arch}", pkg)
        ihdeps.append((sver, f"base-cross-{pprof.arch}", sfull))

    chost = chroot.host_cpu()

    if len(ihdeps) == 0 and len(itdeps) == 0 and len(irdeps) == 0:
        # clear the world
        with flock.lock(flock.apklock(chost)):
            _install_from_repo(pkg, [])
        return False

    hsys = paths.bldroot()
    tsys = hsys
    if cross:
        tsys = tsys / pprof.sysroot.relative_to("/")

    hvers, hrepos = _get_vers(map(lambda v: v[1], ihdeps), pkg, hsys, None)
    tvers, trepos = _get_vers(map(lambda v: v[1], itdeps), pkg, tsys, tarch)
    rvers, rrepos = _get_vers(
        map(
            lambda v: v[0],
            filter(
                lambda v: v[0],
                [autil.split_pkg_name(dep) for origin, dep in irdeps],
            ),
        ),
        pkg,
        tsys,
        tarch,
    )

    depcheck = chroot.get_depcheck()

    for sver, pkgn, fulln in ihdeps:
        if not depcheck:
            host_binpkg_deps.append(pkgn)
            continue
        # check if available in repository
        aver = _is_available(pkgn, "=", sver, pkg, hvers, hrepos, hsys, None)
        if aver:
            log.out_plain(f"  [host] {pkgn}: found ({aver})")
            host_binpkg_deps.append(f"{pkgn}={aver}")
            continue
        # dep finder did not previously resolve a template
        if not sver:
            log.out_plain(f"  [host] {pkgn}: unresolved build dependency")
            pkg.error(f"host dependency '{pkgn}' does not exist")
        # not found
        log.out_plain(f"  [host] {pkgn}: not found")
        # check for loops
        if not cross and (pkgn == origpkg or pkgn == pkg.pkgname):
            pkg.error(f"[host] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        host_missing_deps.append(fulln)
        host_binpkg_deps.append(f"{pkgn}={sver}")

    for sver, pkgn, fulln in itdeps:
        if not depcheck:
            binpkg_deps.append(pkgn)
            continue
        # check if available in repository
        aver = _is_available(pkgn, "=", sver, pkg, tvers, trepos, tsys, tarch)
        if aver:
            log.out_plain(f"  [target] {pkgn}: found ({aver})")
            binpkg_deps.append(f"{pkgn}={aver}")
            continue
        # dep finder did not previously resolve a template
        if not sver:
            log.out_plain(f"  [target] {pkgn}: unresolved build dependency")
            pkg.error(f"target dependency '{pkgn}' does not exist")
        # not found
        log.out_plain(f"  [target] {pkgn}: not found")
        # check for loops
        if pkgn == origpkg or pkgn == pkg.pkgname:
            pkg.error(f"[target] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        missing_deps.append(fulln)
        binpkg_deps.append(f"{pkgn}={sver}")

    for origin, dep in irdeps:
        if not depcheck:
            continue
        pkgn, pkgv, pkgop = autil.split_pkg_name(dep)
        # sanitize
        if not pkgn:
            pkg.error(f"invalid runtime dependency: {dep}")
        # check special cases if guaranteed not to be a loop
        if pkgn != origin:
            # subpackage depending on parent
            if pkgn == pkg.pkgname:
                log.out_plain(f"  [runtime] {dep}: subpackage (ignored)")
                continue
            # parent or another subpackage depending on subpackage
            is_subpkg = False
            for sp in pkg.subpkg_list:
                if sp.pkgname == pkgn:
                    is_subpkg = True
                    break
            if is_subpkg:
                log.out_plain(f"  [runtime] {dep}: subpackage (ignored)")
                continue
        else:
            # if package and its origin are the same, it depends on itself
            pkg.error(f"[runtime] build loop detected: {pkgn} <-> {pkgn}")
        # we're a dependency build but depend on whatever depends on us
        if pkgn == origpkg and pkg.pkgname != origpkg:
            pkg.error(f"[runtime] build loop detected: {pkgn} <-> {pkgn}")
        # check the repository
        aver = _is_available(pkgn, pkgop, pkgv, pkg, rvers, rrepos, tsys, tarch)
        if aver:
            log.out_plain(f"  [runtime] {dep}: found ({aver})")
            continue
        # not found
        log.out_plain(f"  [runtime] {dep}: not found")
        # consider missing
        rdv, fulln = _srcpkg_ver(pkgn, pkg)
        if not fulln or (pkgop and pkgv and not rdv):
            pkg.error(f"template '{pkgn}' cannot be resolved")
        if pkgop and pkgv:
            rfv = f"{pkgn}-{rdv}"
            rpt = pkgn + pkgop + pkgv
            # ensure the build is not futile
            if not autil.pkg_match(rfv, rpt):
                pkg.error(f"version {rfv} does not match dependency {rpt}")
        # treat the same as any missing target dependency, but without install
        missing_deps.append(fulln)

    from cbuild.core import build

    # if this triggers any build of its own, it will return true
    missing = False

    for fulln in host_missing_deps:
        try:
            build.build(
                step,
                template.Template(
                    fulln,
                    chost if pkg.stage > 0 else None,
                    False,
                    pkg.run_check,
                    (pkg.conf_jobs, pkg.conf_link_threads),
                    pkg.build_dbg,
                    (pkg.use_ccache, pkg.use_sccache, pkg.use_ltocache),
                    pkg,
                    force_check=pkg._force_check,
                    stage=pkg.stage,
                    allow_restricted=pkg._allow_restricted,
                    data=pkg._data,
                ),
                depmap,
                chost=hostdep or cross,
                no_update=not missing,
                update_check=update_check,
                maintainer=pkg._maintainer,
            )
            missing = True
        except template.SkipPackage:
            pass

    for fulln in missing_deps:
        try:
            build.build(
                step,
                template.Template(
                    fulln,
                    tarch if pkg.stage > 0 else None,
                    False,
                    pkg.run_check,
                    (pkg.conf_jobs, pkg.conf_link_threads),
                    pkg.build_dbg,
                    (pkg.use_ccache, pkg.use_sccache, pkg.use_ltocache),
                    pkg,
                    force_check=pkg._force_check,
                    stage=pkg.stage,
                    allow_restricted=pkg._allow_restricted,
                    data=pkg._data,
                ),
                depmap,
                chost=hostdep,
                no_update=not missing,
                update_check=update_check,
                maintainer=pkg._maintainer,
            )
            missing = True
        except template.SkipPackage:
            pass

    if len(host_binpkg_deps) > 0 or (len(binpkg_deps) > 0 and not cross):
        tdeps = sorted(
            set(host_binpkg_deps + (binpkg_deps if not cross else []))
        )
        dept = "host" if cross else "build"
        pkg.log(f"installing {dept} dependencies: {', '.join(tdeps)}")
        with flock.lock(flock.apklock(chost)):
            _install_from_repo(pkg, tdeps)
    else:
        # clear the world
        with flock.lock(flock.apklock(chost)):
            _install_from_repo(pkg, [])

    if len(binpkg_deps) > 0 and cross:
        pkg.log(f"installing target dependencies: {', '.join(binpkg_deps)}")
        with flock.lock(flock.apklock(tarch)):
            _install_from_repo(pkg, binpkg_deps, True)

    return missing
