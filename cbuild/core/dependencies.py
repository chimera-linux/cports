from cbuild.core import logger, chroot, template, paths, xbps
from cbuild.step import build as do_build
from cbuild import cpu
from os import path, makedirs

# works on either subpackage or main package
def get_pkg_depends(pkg, with_subpkgs):
    rundeps = []

    if hasattr(pkg, "depends"):
        collected = list(pkg.depends)
    else:
        collected = []

    if with_subpkgs:
        if hasattr(pkg, "subpackages"):
            for sp in pkg.subpkg_list:
                if hasattr(sp, "depends"):
                    collected += sp.depends

    for depname in collected:
        if not with_subpkgs:
            rundeps.append(depname)
            continue
        foo = xbps.get_pkg_dep_name(depname)
        if not foo:
            foo = xbps.get_pkg_name(depname)
            if not foo:
                foo = depname
        rundeps.append(foo)

    return rundeps

def _install_from_repo(pkg, pkglist):
    foo = chroot.invoke_xcmd(xbps.install(), ["-Ay"] + pkglist)
    if foo.returncode != 0:
        outl = foo.stdout.strip().decode("ascii")
        if len(outl) > 0:
            pkg.logger.out_plain(">> stdout:")
            pkg.logger.out_plain(outl)
        outl = foo.stderr.strip().decode("ascii")
        if len(outl) > 0:
            pkg.logger.out_plain(">> stderr:")
            pkg.logger.out_plain(foo.stderr.decode("ascii"))
        pkg.error(f"failed to install dependencies! ({foo.returncode})")

def install(pkg, origpkg, step):
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

    if len(pkg.hostmakedepends) > 0:
        tmpls = []
        for dep in pkg.hostmakedepends:
            if path.isfile(path.join(paths.templates(), dep, "template.py")):
                tmpls.append(dep)
                continue
            rurl = chroot.invoke_query(
                ["-R", "-prepository", dep]
            ).stdout.strip().decode("ascii")
            if len(rurl) > 0:
                log.out_plain(f"   [host] {dep}: found ({rurl})")
                host_binpkg_deps.append(dep)
                continue
            pkg.error(f"host dependency '{dep}' does not exist")
        vers = chroot.invoke_xcmd(xbps.checkvers(), [
            "-D", paths.distdir(), "-sm"
        ] + tmpls).stdout.strip().decode("ascii").split("\n")
        for line in vers:
            if len(line) == 0:
                continue
            flds = line.split()
            depn = flds[0]
            deprv = flds[1]
            depver = flds[2]
            subpkg = flds[3]
            repourl = flds[4]
            vpkg = f"{subpkg}-{depver}"
            # binary package found in repo
            if depver == deprv:
                log.out_plain(f"   [host] {vpkg}: found ({repourl})")
                host_binpkg_deps.append(vpkg)
                continue
            # binary package not found
            if depn != subpkg:
                # subpkg, check if it's a subpkg of itself
                found = False
                for sp in pkg.subpkg_list:
                    if sp.pkgname == subpkg:
                        found = True
                        break
                if found:
                    log.out_plain(
                        f"   [host] {vpkg}: not found (subpkg, ignored)"
                    )
                else:
                    log.out_plain(f"   [host] {vpkg}: not found")
                    host_missing_deps.append(vpkg)
            else:
                log.out_plain(f"   [host] {vpkg}: not found")
                host_missing_deps.append(vpkg)

    if len(pkg.makedepends) > 0:
        tmpls = []
        for dep in pkg.makedepends:
            if path.isfile(path.join(paths.templates(), dep, "template.py")):
                tmpls.append(dep)
                continue
            rurl = chroot.invoke_query(
                ["-R", "-prepository", dep]
            ).stdout.strip().decode("ascii")
            if len(rurl) > 0:
                log.out_plain(f"   [target] {dep}: found ({rurl})")
                binpkg_deps.append(dep)
                continue
            pkg.error(f"target dependency '{dep}' does not exist")
        vers = chroot.invoke_xcmd(xbps.checkvers(), [
            "-D", paths.distdir(), "-sm"
        ] + tmpls).stdout.strip().decode("ascii").split("\n")
        for line in vers:
            if len(line) == 0:
                continue
            flds = line.split()
            depn = flds[0]
            deprv = flds[1]
            depver = flds[2]
            subpkg = flds[3]
            repourl = flds[4]
            vpkg = f"{subpkg}-{depver}"
            # binary package found in repo
            if depver == deprv:
                log.out_plain(f"   [target] {vpkg}: found ({repourl})")
                binpkg_deps.append(vpkg)
                continue
            # binary package not found
            if depn != subpkg:
                # subpkg, check if it's a subpkg of itself
                found = False
                for sp in pkg.subpkg_list:
                    if sp.pkgname == subpkg:
                        found = True
                        break
                if found:
                    pkg.error(f"target dependency '{subpkg}' is a subpackage")
                else:
                    log.out_plain(f"   [target] {vpkg}: not found")
                    missing_deps.append(vpkg)
            else:
                log.out_plain(f"   [target] {vpkg}: not found")
                missing_deps.append(vpkg)

    cleandeps = get_pkg_depends(pkg, True)
    if len(cleandeps) > 0:
        tmpls = []
        for dep in cleandeps:
            if path.isfile(path.join(paths.templates(), dep, "template.py")):
                tmpls.append(dep)
                continue
            rurl = chroot.invoke_query(
                ["-R", "-prepository", dep]
            ).stdout.strip().decode("ascii")
            if len(rurl) > 0:
                log.out_plain(f"   [runtime] {dep}: found ({rurl})")
                continue
            pkg.error(f"target dependency '{dep}' does not exist!")
        vers = chroot.invoke_xcmd(xbps.checkvers(), [
            "-D", paths.distdir(), "-sm"
        ] + tmpls).stdout.strip().decode("ascii").split("\n")
        for line in vers:
            if len(line) == 0:
                continue
            flds = line.split()
            depn = flds[0]
            deprv = flds[1]
            depver = flds[2]
            subpkg = flds[3]
            repourl = flds[4]
            vpkg = f"{subpkg}-{depver}"
            # binary package found in repo
            if depver == deprv:
                log.out_plain(f"   [runtime] {vpkg}: found ({repourl})")
                continue
            # binary package not found
            if depn != subpkg:
                # subpkg, check if it's a subpkg of itself
                found = False
                for sp in pkg.subpkg_list:
                    if sp.pkgname == subpkg:
                        found = True
                        break
                if found:
                    log.out_plain(
                        f"   [runtime] {vpkg}: not found (subpkg, ignored)"
                    )
                else:
                    log.out_plain(f"   [runtime] {vpkg}: not found")
                    missing_rdeps.append(vpkg)
            elif depn == pkg.pkgname:
                log.out_plain(
                    f"   [runtime] {vpkg}: not found (self, ignored)"
                )
            else:
                log.out_plain(f"   [runtime] {vpkg}: not found")
                missing_rdeps.append(vpkg)

    for hd in host_missing_deps:
        pass

    for td in missing_deps:
        pass

    for rd in missing_rdeps:
        pass

    if len(host_binpkg_deps) > 0:
        pkg.log(f"installing host dependencies: {', '.join(host_binpkg_deps)}")
        _install_from_repo(pkg, host_binpkg_deps)

    if len(binpkg_deps) > 0:
        pkg.log(f"installing target dependencies: {', '.join(binpkg_deps)}")
        _install_from_repo(pkg, binpkg_deps)
