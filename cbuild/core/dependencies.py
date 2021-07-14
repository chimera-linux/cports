from cbuild.core import logger, template, paths, chroot
from cbuild.step import build as do_build
from cbuild.apk import util as autil
from cbuild import cpu
from os import makedirs
import subprocess

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

    rv = template.read_pkg(
        pkgn, cpu.target(), False, False, False, False, None
    )
    cv = rv.version + "-r" + str(rv.revision)
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
        pn, pv, pop = autil.split_pkg_name(dep)
        if not pn:
            rdeps.append((orig, dep + ">=0"))
        else:
            rdeps.append((orig, dep))

    for dep in pkg.hostmakedepends:
        sver = _srcpkg_ver(dep)
        if not sver:
            hdeps.append((None, dep))
            continue
        hdeps.append((sver, dep))

    for dep in pkg.makedepends:
        sver = _srcpkg_ver(dep)
        if not sver:
            tdeps.append((None, dep))
            continue
        tdeps.append((sver, dep))

    return hdeps, tdeps, rdeps

def _install_from_repo(pkg, pkglist, virtn, signkey):
    extra_opts = []
    if not signkey:
        extra_opts.append("--allow-untrusted")

    if pkg.bootstrapping:
        ret = subprocess.run([
            "apk", "add", "--root", str(paths.masterdir()),
            "--no-scripts", "--repositories-file",
            str(paths.hostdir() / "repositories"),
            "--virtual", virtn
        ] + extra_opts + pkglist, capture_output = True)
    else:
        ret = chroot.enter(
            "apk", ["add", "--virtual", virtn] + extra_opts + pkglist,
            capture_out = True,
            pretend_uid = 0,
            pretend_gid = 0,
            mount_binpkgs = True
        )
    if ret.returncode != 0:
        outl = ret.stderr.strip().decode()
        if len(outl) > 0:
            pkg.logger.out_plain(">> stderr:")
            pkg.logger.out_plain(outl)
        pkg.error(f"failed to install dependencies")

def _is_installed(pkgn):
    return subprocess.run(["apk", "info", "--root", str(paths.masterdir()),
        "--allow-untrusted", "--repositories-file",
        str(paths.hostdir() / "repositories"),
        "--installed", pkgn
    ], capture_output = True).returncode == 0

def _is_available(pkgn, pattern = None):
    aout = subprocess.run([
        "apk", "search", "-e", "--allow-untrusted", "--root",
        str(paths.masterdir()), "--repositories-file",
        str(paths.hostdir() / "repositories"),
        pkgn
    ], capture_output = True)

    if aout.returncode != 0:
        return None

    pn = aout.stdout.strip().decode()

    if len(pn) == 0:
        return None

    if not pattern or autil.pkg_match(pn, pattern):
        return pn[len(pkgn) + 1:]

    return None

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

    for sver, pkgn in ihdeps:
        # check if already installed
        if _is_installed(pkgn):
            log.out_plain(f"   [host] {pkgn}: installed")
            continue
        # check if available in repository
        aver = _is_available(pkgn, (pkgn + "=" + sver) if sver else None)
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
        if pkgn == origpkg or pkgn == pkg.pkgname:
            pkg.error(f"[host] build loop detected: {pkgn} <-> {origpkg}")
        # build from source
        host_missing_deps.append(pkgn)

    for sver, pkgn in itdeps:
        # check if already installed
        if _is_installed(pkgn):
            log.out_plain(f"   [target] {pkgn}: installed")
            continue
        # check if available in repository
        aver = _is_available(pkgn, (pkgn + "=" + sver) if sver else None)
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
        aver = _is_available(pkgn, dep)
        if aver:
            log.out_plain(f"   [runtime] {dep}: found ({aver})")
            continue
        # not found
        log.out_plain(f"   [runtime] {dep}: not found")
        # consider missing
        missing_rdeps.append(pkgn)

    from cbuild.core import build

    chost = cpu.host()
    ctgt = cpu.target()

    for pn in host_missing_deps:
        try:
            build.build(step, template.read_pkg(
                pn, chost if not pkg.bootstrapping else None,
                pkg.force_mode, True, pkg.build_dbg, pkg.use_ccache, pkg
            ), depmap, signkey)
        except template.SkipPackage:
            pass
        host_binpkg_deps.append(pn)

    for pn in missing_deps:
        try:
            build.build(step, template.read_pkg(
                pn, ctgt if not pkg.bootstrapping else None,
                pkg.force_mode, True, pkg.build_dbg, pkg.use_ccache, pkg
            ), depmap, signkey)
        except template.SkipPackage:
            pass
        binpkg_deps.append(pn)

    for rd in missing_rdeps:
        try:
            build.build(step, template.read_pkg(
                rd, ctgt if not pkg.bootstrapping else None,
                pkg.force_mode, True, pkg.build_dbg, pkg.use_ccache, pkg
            ), depmap, signkey)
        except template.SkipPackage:
            pass
        host_binpkg_deps.append(rd)

    # reinit after parsings
    cpu.init_target(pkg.build_profile)

    if len(host_binpkg_deps) > 0:
        pkg.log(f"installing host dependencies: {', '.join(host_binpkg_deps)}")
        _install_from_repo(pkg, host_binpkg_deps, "autodeps-host", signkey)

    if len(binpkg_deps) > 0:
        pkg.log(f"installing target dependencies: {', '.join(binpkg_deps)}")
        _install_from_repo(pkg, binpkg_deps, "autodeps-target", signkey)
