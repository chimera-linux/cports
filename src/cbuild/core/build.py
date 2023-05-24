from cbuild.step import fetch, extract, prepare, patch, configure
from cbuild.step import build as buildm, check, install, prepkg, pkg as pkgsm
from cbuild.core import chroot, logger, dependencies
from cbuild.core import template, pkg as pkgm, paths, errors
from cbuild.util import flock
from cbuild.apk import cli as apk

import os
import pathlib
import shutil


def build(
    step,
    pkg,
    depmap,
    signkey,
    chost=False,
    dirty=False,
    keep_temp=False,
    check_fail=False,
    no_update=False,
):
    if chost:
        depn = "host-" + pkg.pkgname
    else:
        depn = pkg.pkgname

    if depn in depmap:
        pkg.error(
            f"build-time dependency cycle encountered for {pkg.pkgname} (dependency of {pkg.origin.pkgname})"
        )

    depmap[depn] = True

    pkg.install_done = False
    pkg.current_phase = "setup"

    # always clean up before starting, unless exlpicitly requested not to
    # or unless bootstrapping stage 0 (as resumption is useful by default
    # in there) but not any other stage
    if not dirty and pkg.stage > 0:
        # clean up old state
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    pkg.statedir.mkdir(parents=True, exist_ok=True)
    pkg.wrapperdir.mkdir(parents=True, exist_ok=True)

    pkg.setup_reproducible()

    if not dirty:
        # no_update is set when this is a build triggered by a missing dep;
        # in this case chroot.update() was already performed by its parent
        # call and there is no point in doing it again
        #
        # an exception is when building a second or further missing dependency
        if pkg.stage > 0 and not no_update:
            chroot.update(pkg)

        chroot.remove_autodeps(pkg.stage == 0, pkg.profile())

        # check and install dependencies
        # if a missing dependency has triggered a build, update the chroot
        # afterwards to have a clean state with up to date dependencies
        if dependencies.install(
            pkg, pkg.origin.pkgname, "pkg", depmap, signkey, chost
        ):
            chroot.update(pkg)

    oldcwd = pkg.cwd
    oldchd = pkg.chroot_cwd

    pkg.cwd = pkg.builddir / pkg.wrksrc
    pkg.chroot_cwd = pkg.chroot_builddir / pkg.wrksrc

    # ensure the wrksrc exists; it will be populated later
    pkg.cwd.mkdir(exist_ok=True, parents=True)

    # run up to the step we need
    pkg.current_phase = "fetch"

    srclock = paths.sources() / "cbuild.lock"

    # lock the whole sources dir for the operation
    #
    # while a per-template lock may seem enough,
    # that would still race when sharing sources
    # between templates (which regularly happens)
    with flock.lock(srclock, pkg):
        fetch.invoke(pkg)

    if step == "fetch":
        return

    pkg.current_phase = "extract"
    extract.invoke(pkg)
    if step == "extract":
        return

    pkg.current_phase = "prepare"
    prepare.invoke(pkg)
    if step == "prepare":
        return

    pkg.current_phase = "patch"
    patch.invoke(pkg)
    if step == "patch":
        return

    pkg.cwd = oldcwd
    pkg.chroot_cwd = oldchd

    pkg.current_phase = "configure"
    configure.invoke(pkg, step)
    if step == "configure":
        return
    pkg.current_phase = "build"
    buildm.invoke(pkg, step)
    if step == "build":
        return
    pkg.current_phase = "check"
    check.invoke(pkg, step, check_fail)
    if step == "check":
        return

    # invoke install for main package
    pkg.current_phase = "install"
    install.invoke(pkg, step)
    if step == "install":
        return

    pkg.current_phase = "pkg"
    template.call_pkg_hooks(pkg, "init_pkg")

    for sp in pkg.subpkg_list:
        prepkg.invoke(sp)

    prepkg.invoke(pkg)

    pkg.signing_key = signkey
    pkg._stage = {}

    # package gen + staging is a part of the same lock
    with flock.lock(flock.stagelock(pkg), pkg):
        # generate packages for subpackages
        for sp in pkg.subpkg_list:
            pkgsm.invoke(sp)
        # generate primary packages
        pkgsm.invoke(pkg)
        # stage binary packages
        for repo in pkg._stage:
            logger.get().out(f"Staging new packages to {repo}...")
            if not apk.build_index(repo, pkg.source_date_epoch, signkey):
                raise errors.CbuildException("indexing repositories failed")

    pkg.signing_key = None

    # cleanup
    if not keep_temp:
        chroot.remove_autodeps(pkg.stage == 0, pkg.profile())
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    del depmap[depn]
