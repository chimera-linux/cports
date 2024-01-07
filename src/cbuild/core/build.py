from cbuild.step import fetch, extract, prepare, patch, configure
from cbuild.step import build as buildm, check, install, prepkg, pkg as pkgsm
from cbuild.core import chroot, logger, dependencies
from cbuild.core import template, pkg as pkgm, errors
from cbuild.util import flock
from cbuild.apk import cli as apk


def build(
    step,
    pkg,
    depmap,
    chost=False,
    dirty=False,
    keep_temp=False,
    check_fail=False,
    no_update=False,
    update_check=False,
    accept_checksums=False,
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
    pkg.update_check = update_check
    pkg.accept_checksums = accept_checksums

    pkg.build_lint()

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

    oldcwd = pkg.cwd
    oldchd = pkg.chroot_cwd

    pkg.cwd = pkg.builddir / pkg.wrksrc
    pkg.chroot_cwd = pkg.chroot_builddir / pkg.wrksrc

    # ensure the wrksrc exists; it will be populated later
    pkg.cwd.mkdir(exist_ok=True, parents=True)

    if not hasattr(pkg, "do_fetch"):
        pkg.current_phase = "fetch"
        fetch.invoke(pkg)
        pkg.current_phase = "setup"

        if step == "fetch":
            return

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
            pkg, pkg.origin.pkgname, "pkg", depmap, chost, update_check
        ):
            chroot.update(pkg)

    if hasattr(pkg, "do_fetch"):
        pkg.current_phase = "fetch"
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

    # perform destdir and statedir cleanup
    #
    # this is done before install and makes sure to remove all the
    # sentinels that marked installation from statedir, as well as
    # removes all the destdir stuff, so that dirty builds can always
    # be done cleanly
    if pkg.stage > 0:
        pkgm.remove_pkg(pkg)

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
            if not apk.build_index(repo, pkg.source_date_epoch):
                raise errors.CbuildException("indexing repositories failed")

    # cleanup
    if not keep_temp:
        chroot.remove_autodeps(pkg.stage == 0, pkg.profile())
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    del depmap[depn]
