from cbuild.core import logger, template, paths, xbps, chroot
from cbuild.step import build as do_build
from cbuild import cpu
from os import makedirs

# avoid re-parsing same templates every time; the version will
# never be conditional and that is the only thing we care about
_tcache = {}

def _srcpkg_ver(pkgn):
    global _tcache

    # avoid a failure
    if not (paths.templates() / pkgn / "template.py").is_file():
        return None

    if pkgn in _tcache:
        return _tcache[pkgn]

    rv = template.read_pkg(pkgn, False, False, False, None)
    cv = rv.version + "_" + str(rv.revision)
    _tcache[pkgn] = cv

    return cv

def _setup_depends(pkg):
    hdeps = []
    tdeps = []
    rdeps = []

    crdeps = [(pkg.pkgname, x) for x in pkg.depends]

    # also account for subpackages
    for sp in pkg.subpkg_list:
        for x in sp.depends:
            crdeps.append((sp.pkgname, x))

    for orig, dep in crdeps:
        pd = xbps.get_pkg_dep_name(dep)
        if not pd:
            pd = xbps.get_pkg_name(dep)
        if not pd:
            rdeps.append((orig, dep + ">=0"))
        else:
            rdeps.append((orig, dep))

    for dep in pkg.hostmakedepends:
        sver = _srcpkg_ver(dep)
        if not sver:
            hdeps.append(dep)
            continue
        hdeps.append(dep + "-" + sver)

    for dep in pkg.makedepends:
        sver = _srcpkg_ver(dep)
        if not sver:
            tdeps.append(dep)
            continue
        tdeps.append(dep + "-" + sver)

    return hdeps, tdeps, rdeps

def _install_from_repo(pkg, pkglist, virtn):
    ret = chroot.enter(
        "apk", ["add", "--virtual", virtn] + pkglist, capture_out = True
    )
    if ret.returncode != 0:
        outl = ret.stderr.strip().decode()
        if len(outl) > 0:
            pkg.logger.out_plain(">> stderr:")
            pkg.logger.out_plain(outl)
        pkg.error(f"failed to install dependencies")

def _is_installed(pkgn):
    return chroot.enter("apk", [
        "info", "--installed", pkgn
    ], capture_out = True).returncode == 0

def _is_available(pkgn):
    return chroot.enter("apk", [
        "info", "--description", pkgn
    ], capture_out = True).returncode == 0

def install(pkg, origpkg, step, depmap, signkey):
    style = ""
    if pkg.build_style:
        style = f" [{pkg.build_style}]"

    if pkg.pkgname != origpkg:
        pkg.log(f"building{style} (dependency of {origpkg}) for {cpu.target()}...")
    else:
        pkg.log(f"building{style} for {cpu.target()}...")

    host_binpkg_deps = []
    binpkg_deps = []
    host_missing_deps = []
    missing_deps = []
    missing_rdeps = []

    log = logger.get()

    ihdeps, itdeps, irdeps = _setup_depends(pkg)

    if len(ihdeps) == 0 and len(itdeps) == 0 and len(irdeps) == 0:
        return

    for dep in ihdeps:
        pkgn = xbps.get_pkg_name(dep)
        pkgf = pkgn
        if not pkgn:
            pkgn = dep
        # check if already installed
        if _is_installed(pkgn):
            log.out_plain(f"   [host] {dep}: installed")
            continue
        # check if available in repository
        if _is_available(pkgn):
            log.out_plain(f"   [host] {dep}: found")
            host_binpkg_deps.append(pkgn)
            continue
        # dep finder did not previously resolve a template
        if not pkgf:
            log.out_plain(f"   [host] {dep}: unresolved build dependency")
            pkg.error(f"host dependency '{dep}' does not exist")
        # not found
        log.out_plain(f"   [host] {dep}: not found")
        # check for loops
        if pkgn == origpkg or pkgn == pkg.pkgname:
            pkg.error(f"[host] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        host_missing_deps.append(dep)

    for dep in itdeps:
        pkgn = xbps.get_pkg_name(dep)
        pkgf = pkgn
        if not pkgn:
            pkgn = dep
        # check if already installed
        if _is_installed(pkgn):
            log.out_plain(f"   [target] {dep}: installed")
            continue
        # check if available in repository
        if _is_available(pkgn):
            log.out_plain(f"   [target] {dep}: found")
            binpkg_deps.append(pkgn)
            continue
        # dep finder did not previously resolve a template
        if not pkgf:
            log.out_plain(f"   [target] {dep}: unresolved build dependency")
            pkg.error(f"target dependency '{dep}' does not exist")
        # not found
        log.out_plain(f"   [target] {dep}: not found")
        # check for loops
        if pkgn == origpkg or pkgn == pkg.pkgname:
            pkg.error(f"[target] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        missing_deps.append(dep)

    for origin, dep in irdeps:
        pkgn = xbps.get_pkg_dep_name(dep)
        # sanitize
        if not pkgn:
            pkgn = xbps.get_pkg_name(dep)
            if not pkgn:
                pkg.error(f"invalid runtime dependency: {dep}")
        # check special cases if guaranteed not to be a loop
        if pkgn != origin:
            # subpackage depending on parent
            if pkgn == pkg.pkgname:
                log.out_plain(f"   [runtime] {dep}: subpackage (ignored)")
                continue
            # parent or another subpackage depending on subpackage
            is_subpkg = False
            for sp in pkg.subpkg_list:
                if sp.pkgname == pkgn:
                    is_subpkg = True
                    break
            if is_subpkg:
                log.out_plain(f"   [runtime] {dep}: subpackage (ignored)")
                continue
        else:
            # if package and its origin are the same, it depends on itself
            pkg.error(f"[runtime] build loop detected: {pkgn} <-> {pkgn}")
        # we're a dependency build but depend on whatever depends on us
        if pkgn == origpkg and pkg.pkgname != origpkg:
            pkg.error(f"[runtime] build loop detected: {pkgn} <-> {pkgn}")
        # check the repository
        # FIXME: check version constraints
        if _is_available(pkgn):
            log.out_plain(f"   [runtime] {dep}: found")
            continue
        # not found
        log.out_plain(f"   [runtime] {dep}: not found")
        # consider missing
        missing_rdeps.append(pkgn)

    from cbuild.core import build

    for hd in host_missing_deps:
        pn = xbps.get_pkg_name(hd)
        try:
            build.build(step, template.read_pkg(
                pn, pkg.force_mode, pkg.bootstrapping, True, pkg
            ), depmap, signkey)
        except template.SkipPackage:
            pass
        host_binpkg_deps.append(pn)

    for td in missing_deps:
        pn = xbps.get_pkg_name(td)
        try:
            build.build(step, template.read_pkg(
                pn, pkg.force_mode, pkg.bootstrapping, True, pkg
            ), depmap, signkey)
        except template.SkipPackage:
            pass
        host_binpkg_deps.append(pn)

    for rd in missing_rdeps:
        try:
            build.build(step, template.read_pkg(
                rd, pkg.force_mode, pkg.bootstrapping, True, pkg
            ), depmap, signkey)
        except template.SkipPackage:
            pass
        host_binpkg_deps.append(rd)

    if len(host_binpkg_deps) > 0:
        pkg.log(f"installing host dependencies: {', '.join(host_binpkg_deps)}")
        _install_from_repo(pkg, host_binpkg_deps, "autodeps-host")

    if len(binpkg_deps) > 0:
        pkg.log(f"installing target dependencies: {', '.join(binpkg_deps)}")
        _install_from_repo(pkg, binpkg_deps, "autodeps-target")
