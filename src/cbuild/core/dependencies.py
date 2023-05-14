from cbuild.core import logger, template, paths, chroot
from cbuild.step import build as do_build
from cbuild.apk import util as autil, cli as apki
from os import makedirs
import tempfile
import pathlib
import shutil

# avoid re-parsing same templates every time; the pkgver will
# never be conditional and that is the only thing we care about
_tcache = {}

def _srcpkg_ver(pkgn, pkgb):
    global _tcache

    if pkgn in _tcache:
        return _tcache[pkgn]

    rv = template.read_pkg(
        pkgn, pkgb.profile().arch,
        True, False, (1, 1), False, False, None,
        resolve = pkgb, ignore_missing = True, ignore_errors = True,
        autopkg = True
    )
    if not rv:
        return None

    cv = f"{rv.pkgver}-r{rv.pkgrel}"
    _tcache[pkgn] = cv

    return cv

def _is_rdep(pn):
    if pn.startswith("so:"):
        return False
    elif pn.startswith("pc:"):
        return False
    elif pn.startswith("cmd:"):
        return False
    elif pn.startswith("virtual:"):
        return False

    return True

def setup_depends(pkg, only_names = False):
    hdeps = []
    tdeps = []
    rdeps = []

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
                    f"virtual dependency {dep} has no specified provider"
                )
            dep = dep[ppos + 1:]
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
            sver = _srcpkg_ver(dep, pkg)
            if not sver:
                hdeps.append((None, dep))
                continue
            hdeps.append((sver, dep))
    elif only_names:
        hdeps = pkg.hostmakedepends + cdeps

    if not only_names:
        for dep in pkg.makedepends:
            sver = _srcpkg_ver(dep, pkg)
            if not sver:
                tdeps.append((None, dep))
                continue
            tdeps.append((sver, dep))
    else:
        tdeps = pkg.makedepends

    return hdeps, tdeps, rdeps

def _install_from_repo(pkg, pkglist, virtn, signkey, cross = False):
    # if installing target deps and we're crossbuilding, target the sysroot
    sroot = cross and pkg.profile().cross

    if pkg.stage == 0 or sroot:
        rootp = paths.bldroot()

        if sroot:
            # pretend we're another arch
            # scripts are already never run in this case
            aarch = pkg.profile().arch
            rootp = rootp / pkg.profile().sysroot.relative_to("/")
        else:
            aarch = None

        ret = apki.call(
            "add", ["--no-chown", "--no-scripts", "--virtual", virtn] + pkglist,
            pkg, root = rootp, capture_output = True, arch = aarch,
            allow_untrusted = not signkey
        )
    else:
        if virtn:
            aopts = ["--virtual", virtn] + pkglist
        else:
            aopts = pkglist
        ret = apki.call_chroot(
            "add", aopts, pkg, capture_output = True,
            allow_untrusted = not signkey
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
        pkg.error(f"failed to install dependencies")

def _is_available(pkgn, pattern, pkg, host = False):
    if not host and pkg.profile().cross:
        sysp = paths.bldroot() / pkg.profile().sysroot.relative_to("/")
        aarch = pkg.profile().arch
        crossp = True
    else:
        sysp = paths.bldroot()
        aarch = None
        crossp = False

    aout = apki.call(
        "search", ["--from", "none", "-e", "-a", pkgn], pkg, root = sysp,
        capture_output = True, arch = aarch, allow_untrusted = True
    )

    if aout.returncode != 0:
        return None

    pn = aout.stdout.strip().decode()

    if len(pn) == 0:
        return None

    # FIXME: this list is always sorted alphabetically, ignoring repo
    # order; ideally we want repo order to be respected (because the
    # actual available version may be lower, e.g. when downgrading).
    pn = pn.split("\n")[-1]

    if not pattern or autil.pkg_match(pn, pattern):
        return pn[len(pkgn) + 1:]

    return None

def install(pkg, origpkg, step, depmap, signkey, hostdep):
    style = ""
    if pkg.build_style:
        style = f" [{pkg.build_style}]"

    pprof = pkg.profile()
    tarch = pprof.arch

    if pkg.pkgname != origpkg:
        pkg.log(f"building{style} (dependency of {origpkg}) for {tarch}...")
    else:
        pkg.log(f"building{style} for {tarch}...")

    host_binpkg_deps = []
    binpkg_deps = []
    host_missing_deps = []
    missing_deps = []
    missing_rdeps = []

    log = logger.get()

    ihdeps, itdeps, irdeps = setup_depends(pkg)

    # ensure cross-toolchain is included in hostdeps
    if pprof.cross:
        ihdeps.append((None, f"base-cross-{pprof.arch}"))

    if len(ihdeps) == 0 and len(itdeps) == 0 and len(irdeps) == 0:
        return False

    for sver, pkgn in ihdeps:
        # check if available in repository
        aver = _is_available(
            pkgn, (pkgn + "=" + sver) if sver else None, pkg, host = True
        )
        if aver:
            log.out_plain(f"   [host] {pkgn}: found ({aver})")
            host_binpkg_deps.append(pkgn)
            continue
        # dep finder did not previously resolve a template
        if not sver:
            log.out_plain(f"   [host] {pkgn}: unresolved build dependency")
            pkg.error(f"host dependency '{pkgn}' does not exist")
        # not found
        log.out_plain(f"   [host] {pkgn}: not found")
        # check for loops
        if not pprof.cross and (pkgn == origpkg or pkgn == pkg.pkgname):
            pkg.error(f"[host] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        host_missing_deps.append(pkgn)

    for sver, pkgn in itdeps:
        # check if available in repository
        aver = _is_available(
            pkgn, (pkgn + "=" + sver) if sver else None, pkg
        )
        if aver:
            log.out_plain(f"   [target] {pkgn}: found ({aver})")
            binpkg_deps.append(pkgn)
            continue
        # dep finder did not previously resolve a template
        if not sver:
            log.out_plain(f"   [target] {pkgn}: unresolved build dependency")
            pkg.error(f"target dependency '{pkgn}' does not exist")
        # not found
        log.out_plain(f"   [target] {pkgn}: not found")
        # check for loops
        if pkgn == origpkg or pkgn == pkg.pkgname:
            pkg.error(f"[target] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        missing_deps.append(pkgn)

    for origin, dep in irdeps:
        pkgn, pkgv, pkgop = autil.split_pkg_name(dep)
        # sanitize
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
        aver = _is_available(pkgn, dep, pkg)
        if aver:
            log.out_plain(f"   [runtime] {dep}: found ({aver})")
            continue
        # not found
        log.out_plain(f"   [runtime] {dep}: not found")
        # consider missing
        missing_rdeps.append(pkgn)

    from cbuild.core import build

    chost = chroot.host_cpu()

    # if this triggers any build of its own, it will return true
    missing = False

    for pn in host_missing_deps:
        try:
            build.build(
                step,
                template.read_pkg(
                    pn, chost if pkg.stage > 0 else None, False, pkg.run_check,
                    (pkg.conf_jobs, pkg.conf_link_threads),
                    pkg.build_dbg, pkg.use_ccache, pkg, resolve = pkg,
                    force_check = pkg._force_check, stage = pkg.stage,
                    autopkg = True
                ),
                depmap, signkey, chost = hostdep or not not pprof.cross,
                no_update = not missing
            )
            missing = True
        except template.SkipPackage:
            pass
        host_binpkg_deps.append(pn)

    for pn in missing_deps:
        try:
            build.build(
                step,
                template.read_pkg(
                    pn, tarch if pkg.stage > 0 else None, False, pkg.run_check,
                    (pkg.conf_jobs, pkg.conf_link_threads),
                    pkg.build_dbg, pkg.use_ccache, pkg, resolve = pkg,
                    force_check = pkg._force_check, stage = pkg.stage,
                    autopkg = True
                ),
                depmap, signkey, chost = hostdep, no_update = not missing
            )
            missing = True
        except template.SkipPackage:
            pass
        binpkg_deps.append(pn)

    for rd in missing_rdeps:
        try:
            build.build(
                step,
                template.read_pkg(
                    rd, tarch if pkg.stage > 0 else None, False, pkg.run_check,
                    (pkg.conf_jobs, pkg.conf_link_threads),
                    pkg.build_dbg, pkg.use_ccache, pkg, resolve = pkg,
                    force_check = pkg._force_check, stage = pkg.stage,
                    autopkg = True
                ),
                depmap, signkey, chost = hostdep, no_update = not missing
            )
            missing = True
        except template.SkipPackage:
            pass

    if len(host_binpkg_deps) > 0:
        pkg.log(f"installing host dependencies: {', '.join(host_binpkg_deps)}")
        _install_from_repo(pkg, host_binpkg_deps, "autodeps-host", signkey)

    if len(binpkg_deps) > 0:
        pkg.log(f"installing target dependencies: {', '.join(binpkg_deps)}")
        _install_from_repo(pkg, binpkg_deps, "autodeps-target", signkey, True)

    return missing
