from cbuild.core import chroot, logger, dependencies, profile, scanelf, paths
from cbuild.core import template, update_check as uc, pkg as pkgm, errors
from cbuild.util import flock
from cbuild.apk import cli as apk, generate as apkgen, sign as asign

import builtins
import importlib
import os
import pty
import sys
import shutil
import stat
import termios
import subprocess


def unredir_log(pkg, fpid, oldout, olderr):
    # restore
    os.dup2(oldout, sys.stdout.fileno())
    os.dup2(olderr, sys.stderr.fileno())
    pkg.logger.fileno = sys.stdout.fileno()
    # close the old duplicates
    os.close(oldout)
    os.close(olderr)
    # wait for the logger process to finish
    os.waitpid(fpid, 0)


def sync_winsize(fd, is_pty):
    if not is_pty:
        return
    try:
        if os.isatty(sys.stdout.fileno()):
            termios.tcsetwinsize(fd, termios.tcgetwinsize(sys.stdout))
    except AttributeError:
        # not supported by this version of python
        pass


def redir_log(pkg):
    # save old descriptors
    oldout = os.dup(sys.stdout.fileno())
    olderr = os.dup(sys.stderr.fileno())
    pkg.logger.fileno = oldout
    # child will do the logging for us through a pipe or pty
    prd, prw = None, None
    colors = logger.get().use_colors
    is_pty = False
    try:
        # use a pipe if colors are suppressed, no need for pty
        if colors:
            prd, prw = pty.openpty()
            os.set_inheritable(prd, True)
            os.set_inheritable(prw, True)
            is_pty = True
    except Exception:
        pass
    if not prd:
        prd, prw = os.pipe()
    # read end propagates into child through the fork
    try:
        fpid = os.fork()
    except Exception:
        os.close(prd)
        os.close(prw)
        unredir_log(pkg, fpid, oldout, olderr)
        raise
    # set initial window size
    sync_winsize(prd, is_pty)
    # child
    if fpid == 0:
        os.close(prw)
        try:
            rarr = [bytearray(8192)]
            while True:
                # do this on each loop as the terminal may resize
                sync_winsize(prd, is_pty)
                rlen = os.readv(prd, rarr)
                if rlen == 0:
                    break
                os.write(1, rarr[0][0:rlen])
        finally:
            # raw exit (no exception) since we forked
            # don't want to propagate back to the outside
            #
            # when this triggers in case of failure, the
            # original streams should get restored in the
            # unredir_log function, so we'll lose file logs
            # but retain actual console output (hopefully)
            os._exit(0)
            return
    try:
        # in parent, close read end, we don't need it here
        os.close(prd)
        # everything goes into the pipe/pty
        os.dup2(prw, sys.stdout.fileno())
        os.dup2(prw, sys.stderr.fileno())
        # close original write end too now that it's dup
        os.close(prw)
    except Exception:
        unredir_log(pkg, fpid, oldout, olderr)
        raise
    # fire
    return fpid, oldout, olderr


hooks = {
    "setup": [],
    "fetch": [],
    "extract": [],
    "prepare": [],
    "patch": [],
    "destdir": [],
    "pkg": [],
}


def register_hooks():
    for stepn in hooks:
        dirn = paths.cbuild() / "hooks" / stepn
        if dirn.is_dir():
            for f in dirn.glob("*.py"):
                # this must be skipped
                if f.name == "__init__.py":
                    continue
                modn = "cbuild.hooks." + stepn + "." + f.stem
                modh = importlib.import_module(modn)
                if not hasattr(modh, "invoke"):
                    logger.get().out(
                        f"\f[red]Hook '{stepn}/{f.stem}' does not have an entry point."
                    )
                    raise Exception()
                hooks[stepn].append((modh.invoke, f.stem))
            hooks[stepn].sort(key=lambda v: v[1])


def _restricted_importer(name, globals=None, locals=None, fromlist=(), level=0):
    # a silly way to check if the import is inside the template :)
    if (
        globals
        and "pkgname" in globals
        and "pkgver" in globals
        and "pkgrel" in globals
    ):
        if name != "cbuild.util":
            raise ImportError(
                f"only modules from cbuild.util allowed in template (got: '{name}')"
            )
    return importlib.__import__(name, globals, locals, fromlist, level)


def run_pkg_func(pkg, func, funcn=None, desc=None, on_subpkg=False):
    if not funcn:
        if not hasattr(pkg, func):
            return False
        funcn = func
        func = getattr(pkg, funcn)
    if not desc:
        desc = funcn
    pkg.log(f"running \f[cyan]{desc}\f[]\f[bold]...")
    fpid, oldout, olderr = redir_log(pkg)
    oldimp = builtins.__import__
    builtins.__import__ = _restricted_importer
    try:
        if on_subpkg:
            func()
        else:
            func(pkg)
    finally:
        builtins.__import__ = oldimp
        unredir_log(pkg, fpid, oldout, olderr)
    return True


def call_pkg_hooks(pkg, stepn):
    for f in hooks[stepn]:
        run_pkg_func(
            pkg,
            f[0],
            f"{stepn}_{f[1]}",
            f"{stepn}\f[]\f[bold] hook: \f[orange]{f[1]}",
        )


def _invoke_fetch(pkg):
    run_pkg_func(pkg, "init_fetch")

    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    fetch_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_fetch_done"
    if fetch_done.is_file():
        return

    run_pkg_func(pkg, "pre_fetch")

    if hasattr(pkg, "fetch"):
        pkg.cwd.mkdir(parents=True, exist_ok=True)
        run_pkg_func(pkg, "fetch")
    else:
        call_pkg_hooks(pkg, "fetch")

    run_pkg_func(pkg, "post_fetch")

    fetch_done.touch()


def invoke_fetch(pkg):
    srclock = paths.sources() / "cbuild.lock"

    # lock the whole sources dir for the operation
    #
    # while a per-template lock may seem enough,
    # that would still race when sharing sources
    # between templates (which regularly happens)
    with flock.lock(srclock, pkg):
        _invoke_fetch(pkg)


def invoke_extract(pkg):
    run_pkg_func(pkg, "init_extract")

    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    extract_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_extract_done"
    if extract_done.is_file():
        return

    run_pkg_func(pkg, "pre_extract")

    if hasattr(pkg, "extract"):
        run_pkg_func(pkg, "extract")
    else:
        call_pkg_hooks(pkg, "extract")

    pkg.srcdir.mkdir(parents=True, exist_ok=True)

    run_pkg_func(pkg, "post_extract")

    extract_done.touch()


def invoke_prepare(pkg):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    prepare_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepare_done"

    run_pkg_func(pkg, "init_prepare")

    if prepare_done.is_file():
        return

    call_pkg_hooks(pkg, "prepare")

    run_pkg_func(pkg, "pre_prepare")

    if hasattr(pkg, "prepare"):
        run_pkg_func(pkg, "prepare")

    run_pkg_func(pkg, "post_prepare")

    prepare_done.touch()


def invoke_patch(pkg):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    patch_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_patch_done"

    run_pkg_func(pkg, "init_patch")

    if patch_done.is_file():
        return

    run_pkg_func(pkg, "pre_patch")

    if hasattr(pkg, "patch"):
        run_pkg_func(pkg, "patch")
    else:
        call_pkg_hooks(pkg, "patch")

    run_pkg_func(pkg, "post_patch")

    patch_done.touch()


def invoke_configure(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    cfg_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_configure_done"

    run_pkg_func(pkg, "init_configure")

    if cfg_done.is_file() and (not pkg.force_mode or step != "configure"):
        return

    run_pkg_func(pkg, "pre_configure")
    run_pkg_func(pkg, "configure")
    run_pkg_func(pkg, "post_configure")

    cfg_done.touch()


def invoke_build(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    build_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_build_done"

    run_pkg_func(pkg, "init_build")

    if build_done.is_file() and (not pkg.force_mode or step != "build"):
        return

    run_pkg_func(pkg, "pre_build")
    run_pkg_func(pkg, "build")
    run_pkg_func(pkg, "post_build")

    build_done.touch()


def invoke_check(pkg, step, allow_fail):
    if pkg.profile().cross:
        pkg.log("skipping check (cross build)")
        return

    if not pkg.options["check"] and not pkg._force_check:
        pkg.log("skipping check (disabled by template)")
        return

    if not pkg.run_check:
        pkg.log("skipping check (skipped by user)")
        return

    check_done = pkg.statedir / f"{pkg.pkgname}__check_done"

    run_pkg_func(pkg, "init_check")

    if check_done.is_file() and (not pkg.force_mode or step != "check"):
        return

    try:
        run_pkg_func(pkg, "pre_check")
        run_pkg_func(pkg, "check")
        run_pkg_func(pkg, "post_check")
    except Exception as e:
        if allow_fail:
            pkg.log("check failed, but proceed anyway:")
            print(e)
        else:
            raise

    check_done.touch()


def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)


def _invoke_subpkg(pkg):
    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)
    if pkg.pkg_install:
        run_pkg_func(pkg, "pkg_install", on_subpkg=True)
    # get own licenses by default
    pkg.take(f"usr/share/licenses/{pkg.pkgname}", missing_ok=True)


def _clean_empty(pkg, dpath, auto):
    empty = True

    for f in dpath.iterdir():
        if f.is_dir() and not f.is_symlink():
            if not _clean_empty(pkg, f, auto):
                empty = False
        else:
            empty = False

    if empty and (auto or dpath != pkg.destdir):
        if not auto:
            pr = dpath.relative_to(pkg.destdir)
            pkg.logger.out_plain(f"  \f[orange]clean empty:\f[] {pr}")
        dpath.rmdir()
        return True

    return False


def _split_auto(pkg, done):
    pkg.rparent.subpkg_all.append(pkg)

    pkg.log("\f[cyan]splitting\f[]\f[bold] autopackages...")

    for apkg, adesc, iif, takef in template.autopkgs:
        if takef and not pkg.options["autosplit"]:
            continue
        if apkg == "static" and not pkg.options["splitstatic"]:
            continue
        if apkg == "udev" and not pkg.options["splitudev"]:
            continue
        if apkg == "doc" and not pkg.options["splitdoc"]:
            continue
        if apkg.startswith("dinit") and not pkg.options["splitdinit"]:
            continue
        if pkg.pkgname == iif:
            continue
        if apkg == "dinit-links" and pkg.rparent.pkgname == "dinit-chimera":
            continue
        if pkg.pkgname.endswith(f"-{apkg}"):
            continue

        foundpkg = False
        for sp in pkg.rparent.subpkg_list:
            if sp.pkgname == f"{pkg.pkgname}-{apkg}":
                foundpkg = True
                break
        if foundpkg:
            continue

        sp = template.Subpackage(
            f"{pkg.pkgname}-{apkg}", pkg, pkg.pkgdesc, pkg.subdesc, auto=adesc
        )

        # only take if we're not repeating
        if not done and takef:
            sp.destdir.mkdir(parents=True, exist_ok=True)
            takef(sp)
            # remove if empty
            _clean_empty(sp, sp.destdir, True)

        # now save it only if the destdir still exists
        if sp.destdir.is_dir():
            pkg.rparent.subpkg_all.append(sp)

    # finally clean up empty if needed
    if not done and not pkg.options["keepempty"]:
        _clean_empty(pkg, pkg.destdir, False)

    # create empty dirs as necessary
    for k in pkg.file_modes:
        if not k.startswith("+"):
            continue
        rec = False
        if len(pkg.file_modes[k]) == 4:
            uname, gname, fmode, rec = pkg.file_modes[k]
        else:
            uname, gname, fmode = pkg.file_modes[k]
        (pkg.destdir / k[1:]).mkdir(parents=rec, exist_ok=True, mode=fmode)


def invoke_install(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    install_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done"

    # scan for ELF information after subpackages are split up
    # but before post_install hooks (done by the install step)
    pkg.current_elfs = {}

    # to be populated with Subpackages for current and later use
    pkg.subpkg_all = []

    run_pkg_func(pkg, "init_install")

    if install_done.is_file() and (not pkg.force_mode or step != "install"):
        # when repeating, ensure to at least scan the ELF info...
        for sp in pkg.subpkg_list:
            scanelf.scan(sp, pkg.current_elfs)
            _split_auto(sp, True)
        scanelf.scan(pkg, pkg.current_elfs)
        _split_auto(pkg, True)
        return

    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)

    run_pkg_func(pkg, "pre_install")
    run_pkg_func(pkg, "install")
    run_pkg_func(pkg, "post_install")

    pkg.install_done = True

    for sp in pkg.subpkg_list:
        _invoke_subpkg(sp)
        scanelf.scan(sp, pkg.current_elfs)
        call_pkg_hooks(sp, "destdir")

    scanelf.scan(pkg, pkg.current_elfs)
    call_pkg_hooks(pkg, "destdir")

    # do the splitting at the end to respect e.g. dbg packages
    # empty dir cleaning must be done *after* splitting!
    for sp in pkg.subpkg_list:
        _split_auto(sp, False)
    _split_auto(pkg, False)

    install_done.touch()


def _invoke_prepkg(pkg):
    p = pkg.rparent.profile()
    crossb = p.arch if p.cross else ""
    prepkg_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepkg_done"

    if prepkg_done.is_file() and not pkg.rparent.force_mode:
        return

    call_pkg_hooks(pkg, "pkg")

    prepkg_done.touch()


def invoke_prepkg(pkg):
    for sp in pkg.subpkg_all:
        _invoke_prepkg(sp)


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
    maintainer=None,
):
    pkgm.push(pkg)
    try:
        _build(
            step,
            pkg,
            depmap,
            chost,
            dirty,
            keep_temp,
            check_fail,
            no_update,
            update_check,
            accept_checksums,
            maintainer,
        )
    except Exception:
        pkgm.set_failed(pkgm.pop())
        raise
    pkgm.pop()
    pkg.log(f"finished phase '{step}'")


def _build(
    step,
    pkg,
    depmap,
    chost,
    dirty,
    keep_temp,
    check_fail,
    no_update,
    update_check,
    accept_checksums,
    maintainer,
):
    if chost:
        depn = "host-" + pkg.pkgname
    else:
        depn = pkg.pkgname

    if depn in depmap:
        pkg.error(
            f"build-time dependency cycle encountered for {pkg.pkgname} (dependency of {pkg.origin_pkg.pkgname})"
        )

    depmap[depn] = True

    cfunc = None
    cdep = None

    if step.startswith("custom:"):
        npstep = step.removeprefix("custom:")
        if npstep not in pkg._custom_targets:
            pkg.error(f"custom target '{npstep}' is not defined in template")
        cfunc, cdep = pkg._custom_targets[npstep]

    pkg.install_done = False
    pkg.current_phase = "setup"
    pkg.accept_checksums = accept_checksums

    pkg.setup_paths()
    pkg.setup_vars()
    pkg.build_lint()
    pkg.resolve_depends()

    # always clean up before starting, unless exlpicitly requested not to
    # or unless bootstrapping stage 0 (as resumption is useful by default
    # in there) but not any other stage
    if not dirty and pkg.stage > 0:
        # clean up old state
        pkg.log(f"cleaning build state ({dirty=}, stage={pkg.stage})")
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    pkg.statedir.mkdir(parents=True, exist_ok=True)
    pkg.wrapperdir.mkdir(parents=True, exist_ok=True)

    pkg.setup_reproducible()

    oldcwd = pkg.cwd
    oldchd = pkg.chroot_cwd

    pkg.cwd = pkg.srcdir
    pkg.chroot_cwd = pkg.chroot_srcdir

    pkg._maintainer = maintainer

    prof = pkg.profile()
    hard = profile.get_hardening(prof, pkg)
    hpos = []
    hneg = []
    for hk in hard:
        if hard[hk]:
            hpos.append("+" + hk)
        else:
            hneg.append("-" + hk)

    hpos.sort()
    hneg.sort()

    pkg.log(f"start build (target: {step}), available hardening:")
    pkg.logger.out("\f[green]  " + " ".join(hpos))
    pkg.logger.out("\f[red]  " + " ".join(hneg))

    # ensure the wrksrc exists; it will be populated later
    pkg.cwd.mkdir(exist_ok=True, parents=True)

    # a little DRY abstraction
    def _step_sentinel(stepn):
        if stepn == step:
            return True

        if cdep and cdep == stepn:
            pkg.log(f"running custom target '{npstep}'...")
            cfunc(pkg)
            return True

        return False

    if update_check:
        pkg.log("checking for new versions...")
        uc.check_pkg(pkg)

    if not hasattr(pkg, "fetch"):
        pkg.current_phase = "fetch"
        invoke_fetch(pkg)
        pkg.current_phase = "setup"

        if _step_sentinel("fetch"):
            return

    with flock.lock(flock.rootlock()):
        return _build_locked(
            step,
            pkg,
            depmap,
            depn,
            chost,
            dirty,
            keep_temp,
            check_fail,
            no_update,
            update_check,
            _step_sentinel,
            oldcwd,
            oldchd,
            prof,
        )


def _build_locked(
    step,
    pkg,
    depmap,
    depn,
    chost,
    dirty,
    keep_temp,
    check_fail,
    no_update,
    update_check,
    _step_sentinel,
    oldcwd,
    oldchd,
    prof,
):
    if not dirty or step == "deps":
        # no_update is set when this is a build triggered by a missing dep;
        # in this case chroot.update() was already performed by its parent
        # call and there is no point in doing it again
        #
        # an exception is when building a second or further missing dependency
        if pkg.stage > 0 and not no_update:
            chroot.update(pkg)

        chroot.cleanup_world(pkg.stage == 0, prof, False)

        # check and install dependencies
        # if a missing dependency has triggered a build, update the chroot
        # afterwards to have a clean state with up to date dependencies
        if (
            dependencies.install(
                pkg, pkg.origin_pkg.pkgname, "pkg", depmap, chost, update_check
            )
            and pkg.stage > 0
        ):
            chroot.update(pkg)

    if _step_sentinel("deps"):
        return

    if hasattr(pkg, "fetch"):
        pkg.current_phase = "fetch"
        invoke_fetch(pkg)

        if _step_sentinel("fetch"):
            return

    pkg.current_phase = "extract"
    invoke_extract(pkg)
    if _step_sentinel("extract"):
        return

    if not pkg.prepare_after_patch:
        pkg.current_phase = "prepare"
        invoke_prepare(pkg)
        if _step_sentinel("prepare"):
            return

    pkg.current_phase = "patch"
    invoke_patch(pkg)
    if _step_sentinel("patch"):
        return

    if pkg.prepare_after_patch:
        pkg.current_phase = "prepare"
        invoke_prepare(pkg)
        if _step_sentinel("prepare"):
            return

    pkg.cwd = oldcwd
    pkg.chroot_cwd = oldchd

    call_pkg_hooks(pkg, "setup")

    pkg.current_phase = "configure"
    invoke_configure(pkg, step)
    if _step_sentinel("configure"):
        return
    pkg.current_phase = "build"
    invoke_build(pkg, step)
    if _step_sentinel("build"):
        return
    pkg.current_phase = "check"
    invoke_check(pkg, step, check_fail)
    if _step_sentinel("check"):
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
    invoke_install(pkg, step)
    if _step_sentinel("install"):
        return

    pkg.current_phase = "pkg"
    invoke_prepkg(pkg)

    pkg._stage = {}

    # package gen + staging is a part of the same lock
    with (
        flock.lock(flock.stagelock(pkg), pkg),
        open(pkg.destdir_base / "Makefile", "w") as mkf,
    ):
        pkg.log("generating makefile...")
        # generate makefile for all packages (includes the main one)
        tgts = []
        for sp in pkg.subpkg_all:
            tgts += apkgen.write_make(sp, mkf)
        # make it all phony targets
        mkf.write(f".PHONY: gen {' '.join(tgts)}\n\n")
        # central rule for all packages
        mkf.write(
            f"gen: {' '.join(map(lambda v: v.pkgname, pkg.subpkg_all))}\n"
        )
        mkf.close()
        pkg.log("generating packages...")
        mkcmd = [
            "make",
            "--no-print-directory",
            f"-j{pkg.conf_jobs}",
            "-C",
            str(pkg.chroot_destdir_base),
            "gen",
        ]
        if pkg.stage == 0:
            # a bit scuffed but whatever, simulate "root" with a namespace
            ret = subprocess.run(
                [
                    paths.bwrap(),
                    "--bind",
                    "/",
                    "/",
                    "--uid",
                    "0",
                    "--gid",
                    "0",
                    "--",
                    *mkcmd,
                ]
            )
        else:
            # better, still cannot use pkg.do :(
            ret = chroot.enter(
                *mkcmd,
                ro_root=True,
                ro_build=True,
                ro_dest=False,
                unshare_all=True,
                mount_binpkgs=True,
                fakeroot=True,
                binpkgs_rw=True,
                tmpfiles=[asign.get_keypath()],
            )
        # handle whatever error
        if ret.returncode != 0:
            raise errors.CbuildException("failed to generate packages")
        pkg.current_phase = "index"
        # stage binary packages
        for repo in pkg._stage:
            logger.get().out(f"Staging new packages to {repo}...")
            if not apk.build_index(repo, pkg.source_date_epoch):
                raise errors.CbuildException("indexing repositories failed")

    # cleanup
    pkg.current_phase = "cleanup"
    if not keep_temp:
        chroot.cleanup_world(pkg.stage == 0, pkg.profile(), False)
        pkgm.remove_pkg_wrksrc(pkg)
        pkgm.remove_pkg(pkg)
        pkgm.remove_pkg_statedir(pkg)

    del depmap[depn]
