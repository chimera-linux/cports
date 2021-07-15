from cbuild.step import fetch, extract, patch, configure
from cbuild.step import build as buildm, install, prepkg, pkg as pkgsm
from cbuild.core import chroot, logger, dependencies
from cbuild.core import template, pkg as pkgm, paths
from cbuild.apk import cli as apk

import os

def build(step, pkg, depmap, signkey):
    if pkg.pkgname in depmap:
        pkg.error(f"build-time dependency cycle encountered for {pkg.pkgname} (dependency of {pkg.origin.pkgname})")

    depmap[pkg.pkgname] = True

    # doesn't do anything for native builds
    dependencies.install_toolchain(pkg, signkey)

    # we treat the sysroot as a chimera root
    dependencies.init_sysroot(pkg)

    # remove automatic crossdeps from last time
    dependencies.remove_autocrossdeps(pkg)

    # check and install dependencies
    autodep = dependencies.install(pkg, pkg.origin.pkgname, "pkg", depmap, signkey)

    # run up to the step we need
    fetch.invoke(pkg)
    if step == "fetch":
        return
    extract.invoke(pkg)
    if step == "extract":
        return
    patch.invoke(pkg)
    if step == "patch":
        return
    configure.invoke(pkg, step)
    if step == "configure":
        return
    buildm.invoke(pkg, step)
    if step == "build":
        return

    # invoke install for main package
    install.invoke(pkg, False)

    # scan for ELF information after subpackages are split up
    # but before post_install hooks (done by the install step)
    pkg.current_elfs = {}

    # handle subpackages
    for sp in pkg.subpkg_list:
        install.invoke(sp, True)

    # after subpackages are done, do the same for main package in subpkg mode
    install.invoke(pkg, True)

    template.call_pkg_hooks(pkg, "init_pkg")

    for sp in pkg.subpkg_list:
        prepkg.invoke(sp)

    prepkg.invoke(pkg)

    if step == "install":
        return

    # clear list of preregistered packages
    rp = open(pkg.statedir / f"{pkg.pkgname}_register_pkg", "w")
    rp.close()

    pkg.signing_key = signkey

    # generate binary packages
    for sp in pkg.subpkg_list:
        pkgsm.invoke(sp, paths.repository())

    pkgsm.invoke(pkg, paths.repository())

    # register binary packages

    genrepos = {}

    with open(pkg.statedir / f"{pkg.pkgname}_register_pkg") as f:
        for ln in f:
            repo, pkgn = ln.split(":")
            if not repo in genrepos:
                pkgs = []
                genrepos[repo] = pkgs
            else:
                pkgs = genrepos[repo]
            pkgs.append(pkgn.strip())

    for repo in genrepos:
        logger.get().out(f"Registering new packages to {repo}...")
        if not apk.build_index(repo, pkg.source_date_epoch, signkey):
            logger.get().out_red(f"Indexing apk repositories failed.")
            raise Exception()

    pkg.signing_key = None

    # cleanup
    chroot.remove_autodeps(pkg.bootstrapping)
    dependencies.remove_autocrossdeps(pkg)
    pkgm.remove_pkg_wrksrc(pkg)
    pkgm.remove_pkg(pkg)
    pkgm.remove_pkg_statedir(pkg)

    del depmap[pkg.pkgname]
