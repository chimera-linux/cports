#!/usr/bin/env python3

cbpath = None
rtpath = None

# global options

global_cfg = None
cmdline = None
parser = None

opt_apkcmd = "apk"
opt_apkrepo = "https://repo.chimera-linux.org/current"
opt_bwcmd = "bwrap"
opt_cflags = "-O2"
opt_cxxflags = "-O2"
opt_fflags = "-O2"
opt_timing = True
opt_arch = None
opt_harch = None
opt_gen_dbg = True
opt_check = True
opt_epkgs = ""
opt_ccache = False
opt_sccache = False
opt_tltocache = False
opt_tltocachesize = "10g"
opt_comp = "zstd"
opt_makejobs = 0
opt_lthreads = 0
opt_nocolor = False
opt_signkey = None
opt_force = False
opt_mdirtemp = False
opt_nonet = False
opt_dirty = False
opt_keeptemp = False
opt_forcecheck = False
opt_checkfail = False
opt_stage = False
opt_dryrun = False
opt_altrepo = None
opt_bldroot = "bldroot"
opt_blddir = ""
opt_pkgpath = "packages"
opt_srcpath = "sources"
opt_keypath = None
opt_cchpath = "cbuild_cache"
opt_stagepath = "pkgstage"
opt_statusfd = None
opt_bulkcont = False
opt_allowcat = "main user"
opt_restricted = False
opt_updatecheck = False
opt_acceptsum = False
opt_maint = "unknown <cports@local>"
opt_tdata = {}
opt_nolock = False
opt_nodepcheck = False

#
# INITIALIZATION ROUTINES
#


def init_early():
    import os
    import sys
    import signal
    import os.path

    global cbpath, rtpath

    cbpath = os.path.dirname(os.path.realpath(__file__))
    rtpath = os.path.dirname(cbpath)

    # start from a sane directory
    os.chdir(rtpath)

    # ensure files are created with sane permissions
    os.umask(0o022)

    # we should always be able to import modules from here
    sys.path.append(cbpath)
    # need to be able to import templates
    sys.path.append(rtpath)

    def do_exit(signum, stack):
        from cbuild.core import errors

        raise errors.CbuildException("interrupted!")

    # exit handler
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGTERM, do_exit)


def handle_options():
    import os
    import sys
    import os.path
    import argparse
    import pathlib
    import tempfile
    import configparser

    global global_cfg
    global cmdline
    global parser

    global opt_apkcmd, opt_bwcmd, opt_dryrun, opt_bulkcont, opt_timing
    global opt_arch, opt_tltocache
    global opt_harch, opt_gen_dbg, opt_check, opt_ccache, opt_tltocachesize
    global opt_sccache, opt_makejobs, opt_lthreads, opt_nocolor, opt_signkey
    global opt_force, opt_mdirtemp, opt_allowcat, opt_restricted
    global opt_nonet, opt_dirty, opt_statusfd, opt_keeptemp, opt_forcecheck
    global opt_checkfail, opt_stage, opt_altrepo, opt_stagepath, opt_bldroot
    global opt_blddir, opt_pkgpath, opt_srcpath, opt_cchpath, opt_updatecheck
    global opt_acceptsum, opt_comp, opt_maint, opt_epkgs, opt_tdata, opt_nolock
    global opt_keypath, opt_apkrepo, opt_nodepcheck

    # respect NO_COLOR
    opt_nocolor = ("NO_COLOR" in os.environ) or not sys.stdout.isatty()

    # build epilog
    epilog = ["available commands:"]
    for ch in command_handlers:
        chn = ch
        if len(chn) < 24:
            chn += " " * (20 - len(chn))
        epilog.append(f"  {chn}  {command_handlers[ch][1]}.")

    parser = argparse.ArgumentParser(
        description="Chimera Linux build system.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="\n".join(epilog),
    )

    parser.add_argument(
        "-c",
        "--config",
        default="etc/config.ini",
        help="The configuration file to use.",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_const",
        const=True,
        default=opt_force,
        help="Force writing a package even when it exists and template is older.",
    )
    parser.add_argument(
        "-L",
        "--no-color",
        action="store_const",
        const=True,
        default=opt_nocolor,
        help="Force plain output.",
    )
    parser.add_argument(
        "-W",
        "--force-color",
        action="store_const",
        const=True,
        default=False,
        help="Force color output.",
    )
    parser.add_argument(
        "-j", "--jobs", help="Number of jobs to use.", default=None
    )
    parser.add_argument(
        "-C",
        "--skip-check",
        action="store_const",
        const=True,
        default=not opt_check,
        help="Skip running the check stage.",
    )
    parser.add_argument(
        "--force-check",
        action="store_const",
        const=True,
        default=opt_forcecheck,
        help="Force running check even if disabled by template.",
    )
    parser.add_argument(
        "-X",
        "--check-fail",
        action="store_const",
        const=True,
        default=opt_checkfail,
        help="Do not abort build if check fails.",
    )
    parser.add_argument(
        "-G",
        "--no-dbg",
        action="store_const",
        const=True,
        default=not opt_gen_dbg,
        help="Do not build debug packages.",
    )
    parser.add_argument(
        "-a", "--arch", help="Target architecture to build for.", default=None
    )
    parser.add_argument(
        "-A", "--host-arch", help="Initial host architecture.", default=None
    )
    parser.add_argument(
        "-b", "--build-root", default=None, help="The build root path."
    )
    parser.add_argument(
        "-B", "--build-dir", default=None, help="The path for build/destdir."
    )
    parser.add_argument(
        "-r", "--repository-path", default=None, help="Local repository path."
    )
    parser.add_argument(
        "-R",
        "--alt-repository",
        default=None,
        help="Alternative repository to use.",
    )
    parser.add_argument(
        "-s", "--sources-path", default=None, help="Sources storage path."
    )
    parser.add_argument(
        "-k", "--keys-path", default=None, help="Additional keys path."
    )
    parser.add_argument(
        "-t",
        "--temporary",
        action="store_const",
        const=True,
        default=opt_mdirtemp,
        help="Use a temporary build root.",
    )
    parser.add_argument(
        "-N",
        "--no-remote",
        action="store_const",
        const=True,
        default=opt_nonet,
        help="Do not ever use remote repositories.",
    )
    parser.add_argument(
        "-D",
        "--dirty-build",
        action="store_const",
        const=True,
        default=opt_dirty,
        help="Skip installing (and removing) dependencies.",
    )
    parser.add_argument(
        "-K",
        "--keep-temporary",
        action="store_const",
        const=True,
        default=opt_keeptemp,
        help="Keep temporary files and build dependencies after build.",
    )
    parser.add_argument(
        "--no-depends-check",
        action="store_const",
        const=True,
        default=opt_nodepcheck,
        help="Skip checking of build/run dependency presence/versions.",
    )
    parser.add_argument(
        "--stage",
        action="store_const",
        const=True,
        default=opt_stage,
        help="Keep built packages staged.",
    )
    parser.add_argument(
        "--stage-path", default=None, help="Root path for staged packages."
    )
    parser.add_argument(
        "--dry-run",
        action="store_const",
        const=True,
        default=opt_dryrun,
        help="Do not perform changes to file system (only some commands)",
    )
    parser.add_argument(
        "--status-fd",
        default=None,
        help="File descriptor for bulk build status (must be open).",
    )
    parser.add_argument(
        "--bulk-continue",
        action="store_const",
        const=True,
        default=opt_bulkcont,
        help="Try building the remaining packages in case of bulk failures.",
    )
    parser.add_argument(
        "--update-check",
        action="store_const",
        const=True,
        default=opt_updatecheck,
        help="Perform a update-check before fetching sources.",
    )
    parser.add_argument(
        "--accept-checksums",
        action="store_const",
        const=True,
        default=opt_acceptsum,
        help="Accept mismatched checksums when fetching.",
    )
    parser.add_argument(
        "--no-lock",
        action="store_const",
        const=True,
        default=opt_nolock,
        help="Do not protect paths with advisory locks (dangerous).",
    )
    parser.add_argument(
        "command",
        nargs="+",
        help="The command to issue. See Commands in Usage.md.",
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    cmdline = parser.parse_intermixed_args()

    # parse config file and set the global options from it

    global_cfg = configparser.ConfigParser()
    global_cfg.read(os.path.expanduser(cmdline.config))

    if "apk" in global_cfg:
        apkcfg = global_cfg["apk"]

        opt_apkcmd = apkcfg.get("command", fallback=opt_apkcmd)
        opt_apkrepo = apkcfg.get("repo", fallback=opt_apkrepo)

    if "build" in global_cfg:
        bcfg = global_cfg["build"]

        opt_timing = bcfg.getboolean("timing", fallback=opt_timing)
        opt_gen_dbg = bcfg.getboolean("build_dbg", fallback=opt_gen_dbg)
        opt_ccache = bcfg.getboolean("ccache", fallback=opt_ccache)
        opt_sccache = bcfg.getboolean("sccache", fallback=opt_sccache)
        opt_tltocache = bcfg.getboolean("thinlto_cache", fallback=opt_tltocache)
        opt_check = bcfg.getboolean("check", fallback=opt_check)
        opt_checkfail = bcfg.getboolean("check_fail", fallback=opt_checkfail)
        opt_stage = bcfg.getboolean("keep_stage", fallback=opt_stage)
        opt_makejobs = bcfg.getint("jobs", fallback=opt_makejobs)
        opt_lthreads = bcfg.getint("link_threads", fallback=opt_lthreads)
        opt_tltocachesize = bcfg.get(
            "thinlto_cache_size", fallback=opt_tltocachesize
        )
        opt_bwcmd = bcfg.get("bwrap", fallback=opt_bwcmd)
        opt_arch = bcfg.get("arch", fallback=opt_arch)
        opt_harch = bcfg.get("host_arch", fallback=opt_harch)
        opt_bldroot = bcfg.get("build_root", fallback=opt_bldroot)
        opt_epkgs = bcfg.get("extra_packages", fallback=opt_epkgs)
        opt_blddir = bcfg.get("build_dir", fallback=opt_blddir)
        opt_comp = bcfg.get("compression", fallback=opt_comp)
        opt_stagepath = bcfg.get("stage_repository", fallback=opt_stagepath)
        opt_altrepo = bcfg.get("alt_repository", fallback=opt_altrepo)
        opt_pkgpath = bcfg.get("repository", fallback=opt_pkgpath)
        opt_srcpath = bcfg.get("sources", fallback=opt_srcpath)
        opt_cchpath = bcfg.get("cbuild_cache_path", fallback=opt_cchpath)
        opt_allowcat = bcfg.get("categories", fallback=opt_allowcat)
        opt_maint = bcfg.get("maintainer", fallback=opt_maint)
        opt_restricted = bcfg.getboolean(
            "allow_restricted", fallback=opt_restricted
        )
        opt_nonet = not bcfg.getboolean("remote", fallback=not opt_nonet)

    if "flags" not in global_cfg:
        global_cfg["flags"] = {}

    if "CFLAGS" not in global_cfg["flags"]:
        global_cfg["flags"]["CFLAGS"] = opt_cflags

    if "CXXFLAGS" not in global_cfg["flags"]:
        global_cfg["flags"]["CXXFLAGS"] = opt_cxxflags

    if "FFLAGS" not in global_cfg["flags"]:
        global_cfg["flags"]["FFLAGS"] = opt_fflags

    if "signing" in global_cfg:
        signcfg = global_cfg["signing"]

        opt_signkey = signcfg.get("key", fallback=opt_signkey)
        opt_keypath = signcfg.get("keys", fallback=opt_keypath)

    if "data" in global_cfg:
        opt_tdata = dict(global_cfg["data"])

    # command line args override config file

    if cmdline.jobs:
        opt_makejobs = int(cmdline.jobs)

    if cmdline.no_dbg:
        opt_gen_dbg = False

    if cmdline.arch:
        opt_arch = cmdline.arch

    if cmdline.host_arch:
        opt_harch = cmdline.host_arch

    if cmdline.no_color:
        opt_nocolor = True

    if cmdline.force_color:
        opt_nocolor = False

    if cmdline.force:
        opt_force = True

    if cmdline.skip_check:
        opt_check = False

    if cmdline.build_root:
        opt_bldroot = cmdline.build_root

    if cmdline.build_dir:
        opt_blddir = cmdline.build_dir

    if cmdline.repository_path:
        opt_pkgpath = cmdline.repository_path

    if cmdline.stage_path:
        opt_stagepath = cmdline.stage_path

    if cmdline.alt_repository:
        opt_altrepo = cmdline.alt_repository

    if cmdline.sources_path:
        opt_srcpath = cmdline.sources_path

    if cmdline.keys_path:
        opt_keypath = cmdline.keys_path

    if cmdline.no_remote:
        opt_nonet = True

    if cmdline.no_lock:
        opt_nolock = True

    if cmdline.dirty_build:
        opt_dirty = True

    if cmdline.keep_temporary:
        opt_keeptemp = True

    if cmdline.force_check:
        opt_forcecheck = True

    if cmdline.check_fail:
        opt_checkfail = True

    if cmdline.no_depends_check:
        opt_nodepcheck = True

    if cmdline.temporary:
        mdp = pathlib.Path.cwd() / opt_bldroot
        # the temporary directory should be in the same location as build root
        opt_mdirtemp = True
        opt_bldroot = tempfile.mkdtemp(prefix=mdp.name + ".", dir=mdp.parent)

    if cmdline.stage:
        opt_stage = True

    if cmdline.dry_run:
        opt_dryrun = True

    if cmdline.status_fd:
        opt_statusfd = int(cmdline.status_fd)

    if cmdline.bulk_continue:
        opt_bulkcont = True

    if cmdline.update_check:
        opt_updatecheck = True

    if cmdline.accept_checksums:
        opt_acceptsum = True

    ncores = len(os.sched_getaffinity(0))

    if opt_makejobs == 0:
        opt_makejobs = ncores

    if opt_lthreads == 0:
        opt_lthreads = opt_makejobs


def init_late():
    import os

    from cbuild.core import paths, spdx
    from cbuild.apk import sign, util as autil

    mainrepo = opt_altrepo
    altrepo = opt_pkgpath
    if not mainrepo:
        mainrepo = opt_pkgpath
        altrepo = None

    # init paths early, modules rely on it
    paths.init(
        cbpath,
        rtpath,
        opt_bldroot,
        opt_blddir,
        mainrepo,
        altrepo,
        opt_stagepath,
        opt_srcpath,
        opt_cchpath,
    )

    # apk command
    if "CBUILD_APK_PATH" in os.environ:
        paths.set_apk(os.environ["CBUILD_APK_PATH"])
    else:
        paths.set_apk(opt_apkcmd)

    # bwrap command
    if "CBUILD_BWRAP_PATH" in os.environ:
        paths.set_bwrap(os.environ["CBUILD_BWRAP_PATH"])
    else:
        paths.set_bwrap(opt_bwcmd)

    # init license information
    spdx.init()

    # register signing key
    sign.register_key(opt_signkey)

    if opt_keypath:
        paths.init_keys(opt_keypath)
    else:
        kp = sign.get_keypath()
        if kp:
            paths.init_keys(kp.parent)
        else:
            # fallback
            paths.init_keys("etc/keys")

    # set compression type
    autil.set_compression(opt_comp)


#
# ACTIONS
#


def short_traceback(e, log):
    import traceback
    import subprocess
    import shlex
    from cbuild.core import pkg as pkgm

    log.out("Stack trace:")
    # filter out some pointless stuff:
    # 1) anything coming from inside python at the end (don't care)
    # 2) runner.py entries at the beginning if there's more (also don't care)
    stk = list(traceback.extract_tb(e.__traceback__))
    # first the python ones
    while len(stk) > 0:
        if not stk[-1].filename.startswith(rtpath):
            stk.pop()
        else:
            break
    # now the runner.pys if needed
    if len(stk) > 0 and not stk[-1].filename.endswith("/runner.py"):
        nrunner = 0
        for fs in stk:
            if not fs.filename.endswith("/runner.py"):
                break
            nrunner += 1
        stk = stk[nrunner:]
    # print whatever is left
    for fs in stk:
        log.out(f"  {fs.filename}:{fs.lineno}:", end="")
        log.out_plain(f" in function '{fs.name}'")
    log.out("Raised exception:")
    if hasattr(e, "filename"):
        log.out(f"  {type(e).__name__} ({e.filename}): ", end="")
    else:
        log.out(f"  {type(e).__name__}: ", end="")
    match type(e):
        case subprocess.CalledProcessError:
            # a bit nicer handling of cmd
            # for bwrap commands, skip all the pointless parts of the cmdline
            fcmd = []
            in_bwrap = False
            for ce in map(lambda v: str(v), e.cmd):
                if ce == "bwrap":
                    in_bwrap = True
                    fcmd += ["bwrap", "..."]
                elif ce == "--":
                    in_bwrap = False
                    fcmd.append("--")
                elif not in_bwrap:
                    fcmd.append(ce)
            # now print the command in a nice quoted way
            log.out_plain(
                f"command '{shlex.join(fcmd)}' failed with exit code {e.returncode}"
            )
        case _:
            log.out_plain(str(e))
    curpkg = pkgm.failed()
    if curpkg:
        if hasattr(curpkg, "current_phase"):
            log.out(
                f"\f[orange]Phase '{curpkg.current_phase}' failed for package '{curpkg.pkgname}'."
            )
        else:
            log.out(
                f"\f[orange]Failure during build of package '{curpkg.pkgname}'."
            )


def pkg_error(e, log):
    if e.quiet:
        return
    e.pkg.log_red(f"ERROR: {e}", e.end)
    if e.hint:
        e.pkg.logger.out_plain(
            f"  \f[bold,green]hint:\f[] \f[bold]{e.hint}\f[]"
        )
    if e.bt:
        short_traceback(e, log)


def pkg_run_exc(f):
    from cbuild.core import template, errors, logger

    log = logger.get()
    try:
        retv = f()
        if retv:
            return retv, False
    except template.SkipPackage:
        return False, False
    except errors.CbuildException as e:
        log.out(f"\f[red]cbuild: {e!s}")
        if e.extra:
            log.out_plain(e.extra)
        return False, True
    except errors.TracebackException as e:
        log.out("\f[red]" + str(e))
        short_traceback(e, log)
        return False, True
    except errors.PackageException as e:
        pkg_error(e, log)
        return False, True
    except Exception as e:
        log.out("\f[red]A failure has occurred!")
        short_traceback(e, log)
        return False, True
    return True, False


def binary_bootstrap(tgt):
    from cbuild.core import chroot, paths

    paths.prepare()
    chroot.install()


def do_unstage(tgt, force=False):
    from cbuild.core import chroot, stage

    if opt_arch and opt_arch != chroot.host_cpu():
        stage.clear(opt_arch, force)

    if stage.clear(chroot.host_cpu(), force):
        return 0
    else:
        return 32


def check_unstage(tgt):
    from cbuild.core import chroot, stage

    if opt_arch and opt_arch != chroot.host_cpu():
        stage.check_stage(opt_arch, remote=True)

    stage.check_stage(chroot.host_cpu(), remote=True)


def bootstrap(tgt):
    import sys
    import shutil

    from cbuild.core import build, chroot, logger, template, paths
    from cbuild.apk import cli

    # source bootstrap is always networkless
    cli.set_network(False)

    max_stage = 2

    if len(cmdline.command) > 1:
        max_stage = int(cmdline.command[1])

    oldmdir = paths.bldroot()

    paths.set_stage(0)
    paths.reinit_buildroot(oldmdir, 0)

    if not chroot.chroot_check(True, False):
        logger.get().out("cbuild: bootstrapping stage 0")

        # extra program checks
        for prog in [
            "clang",
            "lld",
            "cmake",
            "meson",
            "patch",
            "pkg-config",
            "make",
            "ninja",
            "strip",
            "yacc",
            "flex",
            "perl",
            "m4",
        ]:
            if not shutil.which(prog):
                sys.exit(f"Required bootstrap program not found: {prog}")

        rp = None
        try:
            rp = template.Template(
                "main/base-cbuild",
                None,
                False,
                False,
                (opt_makejobs, opt_lthreads),
                False,
                False,
                None,
                stage=0,
                data=opt_tdata,
            )
        except template.SkipPackage:
            pass
        paths.prepare()
        chroot.initdb()
        chroot.repo_init()
        if rp:
            build.build(tgt, rp, {}, maintainer=opt_maint)
        do_unstage(tgt, True)
        shutil.rmtree(paths.bldroot())
        chroot.install()

    if max_stage == 0:
        return

    # change binary repo path
    paths.set_stage(1)
    # set build root to stage 1 for chroot check
    paths.reinit_buildroot(oldmdir, 1)

    if not chroot.chroot_check(True, False):
        logger.get().out("cbuild: bootstrapping stage 1")
        # use stage 0 build root to build, but build into stage 1 repo
        paths.reinit_buildroot(oldmdir, 0)
        # make sure to reset chroot_ready when the bldroot is reinited
        chroot.chroot_check(True)
        try:
            do_pkg("pkg", "main/base-cbuild", False, False, stage=1)
        except template.SkipPackage:
            pass
        # go back to stage 1
        paths.reinit_buildroot(oldmdir, 1)
        # now do it again to allow it to install
        chroot.chroot_check(True, False)
        chroot.install()

    if max_stage == 1:
        return

    # change binary repo path
    paths.set_stage(2)
    # set build root to stage 2 for chroot check
    paths.reinit_buildroot(oldmdir, 2)

    if not chroot.chroot_check(True, False):
        logger.get().out("cbuild: bootstrapping stage 2")
        # use stage 1 build root to build, but build into stage 2 repo
        paths.reinit_buildroot(oldmdir, 1)
        chroot.chroot_check(True)
        try:
            do_pkg("pkg", "main/base-cbuild", False, False, stage=2)
        except template.SkipPackage:
            pass
        # go back to stage 2
        paths.reinit_buildroot(oldmdir, 2)
        chroot.chroot_check(True, False)
        chroot.install()

    # change binary repo path
    paths.set_stage(3)
    # set build root to stage 3 for chroot check
    paths.reinit_buildroot(oldmdir, 3)

    if not chroot.chroot_check(True, False):
        logger.get().out("cbuild: bootstrapping stage 3")
        # use stage 1 build root to build, but build into stage 2 repo
        paths.reinit_buildroot(oldmdir, 2)
        chroot.chroot_check(True)
        try:
            do_pkg("pkg", "main/base-cbuild", False, stage=3)
        except template.SkipPackage:
            pass
        # go back to stage 3
        paths.reinit_buildroot(oldmdir, 3)
        chroot.chroot_check(True, False)
        chroot.install()


def bootstrap_update(tgt):
    from cbuild.core import chroot
    from cbuild.util import flock

    chroot.install()
    with flock.lock(flock.rootlock()):
        chroot.cleanup_world(False)
        chroot.update("main")


def do_keygen(tgt):
    import os.path

    from cbuild.apk import sign

    if len(cmdline.command) >= 3:
        keyn, keysize = cmdline.command[1], int(cmdline.command[2])
    elif len(cmdline.command) >= 2:
        keyn, keysize = cmdline.command[1], 2048
    else:
        keyn, keysize = None, 2048

    if not keyn or len(keyn) == 0:
        keyn = None
        sign.register_key(opt_signkey)

    sign.keygen(keysize, keyn, global_cfg, os.path.expanduser(cmdline.config))


def do_clean(tgt):
    import shutil

    from cbuild.core import paths, chroot, template, logger

    ctmpl = cmdline.command[1] if len(cmdline.command) >= 2 else None
    if ctmpl:
        tmpl = template.Template(
            ctmpl,
            chroot.host_cpu(),
            True,
            False,
            (1, 1),
            False,
            False,
            None,
            target="lint",
        )
    else:
        tmpl = None

    chroot.cleanup_world(None)

    for dirn in ["builddir", "destdir"]:
        dirp = paths.builddir() / dirn
        if tmpl:
            dirp = dirp / f"{tmpl.pkgname}-{tmpl.pkgver}"
        if not dirp.exists():
            continue
        logger.get().out(f"cleaning '{dirp}'...")
        if dirp.is_dir():
            shutil.rmtree(dirp)
        else:
            dirp.unlink()


def do_zap(tgt):
    import shutil

    from cbuild.core import paths, errors

    if paths.bldroot().is_dir():
        shutil.rmtree(paths.bldroot())
    elif paths.bldroot().exists():
        raise errors.CbuildException("broken build container")


def do_remove_autodeps(tgt):
    from cbuild.core import chroot

    chroot.cleanup_world(None)


def do_prune_obsolete(tgt):
    from cbuild.core import logger, paths
    from cbuild.apk import cli

    logger.get().out("cbuild: pruning repositories...")

    reposd = paths.repository()
    reposet = {}

    for idx in cli.find_indexes(reposd):
        repop = idx.parent.parent
        if not repop.is_relative_to(reposd):
            continue
        # only prune once
        if str(repop) in reposet:
            continue
        reposet[str(repop)] = True
        cli.prune(repop, opt_arch, opt_dryrun)


def do_prune_removed(tgt):
    import time

    from cbuild.core import chroot, logger, paths, template, errors
    from cbuild.apk import cli

    # FIXME: compute from git if possible
    epoch = int(time.time())
    # do specific arch only
    archn = opt_arch
    if not archn:
        archn = chroot.host_cpu()

    # pruner for a single repo
    def _prune(repo):
        logger.get().out(f"Pruning removed packages at '{repo}/{archn}'...")
        # find which repo we are looking at
        repon = repo.name
        if not (paths.distdir() / repon).is_dir():
            # this could be a sub-repo
            repon = repo.parent.name
        if not (paths.distdir() / repon).is_dir():
            raise errors.CbuildException(
                f"repository '{repo}' does not match templates"
            )
        tmplp = paths.distdir() / repon
        touched = False
        for pkg in (repo / archn).glob("*.apk"):
            pkgn = pkg.stem
            rd = pkgn.rfind("-")
            if rd > 0:
                rd = pkgn.rfind("-", 0, rd)
            if rd < 0:
                logger.get().out(
                    f"\f[orange]WARNING: Malformed file name found, skipping: {pkg.name}"
                )
                continue
            pkgn = pkgn[0:rd]
            # automatic subpackages are special, except when explicit
            opkgn = pkgn
            if not (tmplp / pkgn / "template.py").exists():
                for apkg, adesc, iif, takef in template.autopkgs:
                    if pkgn.endswith(f"-{apkg}"):
                        pkgn = pkgn[: -len(apkg) - 1]
                        break
            # if it's ok, just skip
            if (tmplp / pkgn / "template.py").exists():
                if pkgn != opkgn:
                    # for autopkgs also check pkgver matches
                    # autopkg always matches its base no matter what
                    bppath = pkg.with_name(pkg.name.replace(opkgn, pkgn))
                    if opkgn.endswith("-dbg"):
                        # if checking dbg, switch repository too
                        bparch = bppath.parent.name
                        bproot = bppath.parent.parent.parent
                        bppath = bproot / bparch / bppath.name
                    if bppath.exists():
                        continue
                else:
                    continue
            # not ok, first test if it's a broken symlink
            broken = True
            try:
                (tmplp / pkgn).lstat()
            except FileNotFoundError:
                broken = False
            if broken:
                logger.get().out(
                    f"\f[orange]WARNING: Broken symlink for package '{pkgn}'"
                )
            logger.get().out(f"Pruning package: {pkg.name}")
            if not opt_dryrun:
                touched = True
                pkg.unlink()
        # reindex
        if touched:
            cli.build_index(repo / archn, epoch)

    reposd = paths.repository()
    reposet = {}
    # find all existing indexes
    for idx in cli.find_indexes(reposd):
        repo = idx.parent.parent
        if not repo.is_relative_to(reposd):
            continue
        # only index once
        if str(repo) in reposet:
            continue
        reposet[str(repo)] = True
        # leave out repos that do not have our arch
        if not (repo / archn).is_dir():
            continue
        # finally index
        _prune(repo)


def do_prune_pkgs(cmd):
    do_prune_obsolete(cmd)
    do_prune_removed(cmd)


def do_index(tgt):
    import time
    import pathlib

    from cbuild.core import chroot, logger, paths, errors
    from cbuild.apk import cli

    idir = cmdline.command[1] if len(cmdline.command) >= 2 else None
    # FIXME: compute from git if possible
    epoch = int(time.time())
    # do specific arch only
    archn = opt_arch
    if not archn:
        archn = chroot.host_cpu()

    # indexer for a single repo
    def _index(repo):
        logger.get().out(f"Indexing packages at '{repo}'...")
        cli.build_index(repo / archn, epoch)

    # only a specific path
    if idir:
        repo = pathlib.Path(idir)
        if not (repo / archn).is_dir():
            raise errors.CbuildException(f"repository '{repo}' does not exist")
        _index(repo)
        return
    # all repos
    reposd = paths.repository()
    reposet = {}
    # find all existing indexes
    for idx in cli.find_indexes(reposd):
        repo = idx.parent.parent
        if not repo.is_relative_to(reposd):
            continue
        # only index once
        if str(repo) in reposet:
            continue
        reposet[str(repo)] = True
        # leave out repos that do not have our arch
        if not (repo / archn).is_dir():
            continue
        # finally index
        _index(repo)


def do_lint(tgt):
    from cbuild.core import chroot, template

    pkgn = cmdline.command[1] if len(cmdline.command) >= 2 else None
    # just read it and do nothing else
    # don't let the skip logic kick in
    template.Template(
        pkgn,
        opt_arch if opt_arch else chroot.host_cpu(),
        True,
        False,
        (1, 1),
        False,
        False,
        None,
        target="lint",
    ).build_lint()


def _collect_tmpls(pkgn, catn=None):
    from cbuild.core import paths

    tmpls = []

    def _scan_cat(cat):
        for tmpl in cat.iterdir():
            if tmpl.is_symlink() or not tmpl.is_dir():
                continue
            pathf = tmpl / "template.py"
            if pathf.exists() and pathf.is_file():
                tmpls.append(f"{cat.name}/{tmpl.name}")

    if catn:
        _scan_cat(paths.distdir() / catn)
    elif pkgn:
        tmpls.append(pkgn)
    else:
        for cat in paths.distdir().iterdir():
            if cat.is_symlink() or not cat.is_dir():
                continue
            _scan_cat(cat)

    tmpls.sort()

    return tmpls


def _add_deps_graph(pn, tp, pvisit, cbvisit, rpkg, depg):
    bdl = tp.get_build_deps()
    depg.add(pn, *bdl)
    # recursively eval and add deps
    succ = True
    for d in bdl:
        if cbvisit is not None:
            cbvisit.add(d)
        if d in pvisit:
            continue
        # make sure that everything is parsed only once
        pvisit.add(d)
        dtp = rpkg(d)
        if dtp:
            if not _add_deps_graph(d, dtp, pvisit, cbvisit, rpkg, depg):
                succ = False
        else:
            succ = False
    return succ


def _graph_prepare():
    import graphlib

    from cbuild.core import chroot, template, errors

    pkgn = cmdline.command[1] if len(cmdline.command) >= 2 else None

    rtmpls = {}

    def _read_pkg(pkgn):
        if pkgn in rtmpls:
            return rtmpls[pkgn]
        try:
            tp = template.Template(
                pkgn,
                chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
            rtmpls[pkgn] = tp
            return tp
        except errors.PackageException:
            return None

    tg = graphlib.TopologicalSorter()
    tmpls = _collect_tmpls(pkgn)
    pvisit = set()
    for tmpln in tmpls:
        # already added in another graph
        if tmpln in pvisit:
            continue
        tp = _read_pkg(tmpln)
        if not tp:
            continue
        _add_deps_graph(tmpln, tp, pvisit, None, _read_pkg, tg)

    return tg


def do_prune_sources(tgt):
    from cbuild.core import chroot, logger, template, errors, paths
    import shutil
    import re

    logger.get().out("Collecting templates...")
    tmpls = _collect_tmpls(None)
    exist = set()

    def _read_pkg(pkgn):
        try:
            tp = template.Template(
                pkgn,
                chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
            exist.add(f"{tp.pkgname}-{tp.pkgver}")
        except errors.PackageException:
            return None

    logger.get().out("Reading templates...")
    for tmpln in tmpls:
        _read_pkg(tmpln)

    logger.get().out("Collecting checksums...")
    shaset = set()
    for tmpln in tmpls:
        with (paths.distdir() / tmpln / "template.py").open("r") as inf:
            for ln in inf.readlines():
                for sha in re.findall(r'"[0-9a-fA-F]{64}"', ln):
                    shaset.add(sha.strip('"').lower())
    shalist = list(shaset)
    shalist.sort()

    def _prune_path(f):
        if opt_dryrun:
            return
        if f.is_dir() and not f.is_symlink():
            shutil.rmtree(f)
        else:
            f.unlink()

    logger.get().out("Collecting inodes and pruning hardlinks...")
    inoset = set()
    (paths.sources() / "by_sha256").mkdir(parents=True, exist_ok=True)
    for sf in (paths.sources() / "by_sha256").iterdir():
        cks = sf.name[0:64].lower()
        if (
            len(cks) != 64
            or cks not in shalist
            or not sf.is_file()
            or sf.is_symlink()
        ):
            logger.get().out(f"Prune hardlink: {sf.name}")
            _prune_path(sf)
            continue
        inoset.add(sf.lstat().st_ino)

    logger.get().out("Pruning sources...")
    # first prune versions that are gone
    for f in paths.sources().iterdir():
        if f.name == "by_sha256" or f.name == "cbuild.lock":
            continue
        # stuff that does not correspond to any template version
        if f.name not in exist:
            logger.get().out(f"Prune orphaned: {f.name}")
            _prune_path(f)
            continue
        # non-dirs in toplevel path
        if not f.is_dir() or f.is_symlink():
            logger.get().out(f"Prune spurious: {f.name}")
            _prune_path(f)
            continue
        # otherwise iterate and prune untracked
        for sf in f.iterdir():
            if sf.lstat().st_ino not in inoset:
                logger.get().out(f"Prune untracked: {sf.name}")
                _prune_path(sf)
        # otherwise we good
        continue

    logger.get().out("Sources pruning complete.")


def do_relink_subpkgs(tgt):
    from cbuild.core import chroot, paths, logger, errors, template
    import shutil

    ddir = paths.distdir()
    links = {}
    cats = {}

    def _read_pkg(pkgn):
        try:
            tp = template.Template(
                pkgn,
                chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
            links[tp.full_pkgname] = tp.all_subpackages
            return tp
        except errors.PackageException:
            return None

    tgt = None
    prune_bad = False

    if len(cmdline.command) >= 2:
        if cmdline.command[1] == "prune":
            prune_bad = True
        else:
            tgt = cmdline.command[1]
            _read_pkg(tgt)

    if not tgt:
        logger.get().out("Collecting templates...")
        tmpls = _collect_tmpls(None)
        logger.get().out("Reading templates...")
        for tmpln in tmpls:
            tp = _read_pkg(tmpln)
            if tp:
                cats[tp.repository] = True
            else:
                logger.get().out(
                    f"\f[orange]WARNING: template '{tmpln}' failed to parse (ignoring)"
                )

    # erase all symlinks first if parsing all
    for d in cats:
        for el in (ddir / d).iterdir():
            if el.name == ".parent" and el.is_symlink():
                continue
            if el.is_symlink():
                if el.name == ".parent":
                    continue
                # symlink, erase
                el.unlink()
            elif el.is_dir():
                if not (el / "template.py").is_file():
                    if prune_bad:
                        logger.get().out(f"Pruning bad directory: {el}")
                        shutil.rmtree(el)
                    else:
                        logger.get().out(
                            f"\f[orange]WARNING: Bad directory encountered: {el}"
                        )
                continue
            elif prune_bad:
                logger.get().out(f"Pruning bad contents: {el}")
                el.unlink()
            else:
                logger.get().out(
                    f"\f[orange]WARNING: Bad contents encountered: {el}"
                )
                continue

    # recreate symlinks
    for pn in links:
        repo, jpn = pn.split("/")
        for sn in links[pn]:
            fp = ddir / repo / sn
            if fp.exists():
                if not fp.is_symlink():
                    logger.get().out(
                        f"\f[orange]WARNING: Non-symlink encountered: {fp}"
                    )
                fp.unlink()
            fp.symlink_to(jpn)


def do_cycle_check(tgt):
    import graphlib

    from cbuild.core import errors

    tg = _graph_prepare()

    try:
        tg.prepare()
    except graphlib.CycleError as ce:
        raise errors.CbuildException(
            "cycle encountered: " + " <= ".join(ce.args[1])
        )


def do_print_build_graph(tgt):
    from cbuild.core import chroot, template, errors

    if len(cmdline.command) < 2:
        raise errors.CbuildException("print-build-graph needs a package name")

    rtmpls = {}

    def _read_pkg(pkgn):
        if pkgn in rtmpls:
            return rtmpls[pkgn]
        try:
            tp = template.Template(
                pkgn,
                opt_arch or chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
            rtmpls[pkgn] = tp
            return tp
        except errors.PackageException:
            return None

    root = _read_pkg(cmdline.command[1])

    built = set()

    def _print_deps(tp, level=0):
        for i in range(level):
            print(end=" ")
        print(f"{tp.pkgname}")
        for dep in tp.get_build_deps():
            if dep in built:
                continue
            built.add(dep)
            _print_deps(_read_pkg(dep), level + 1)

    _print_deps(root)


def _get_unbuilt(outdated=False):
    from cbuild.core import chroot, template, paths
    from cbuild.apk import util
    import subprocess

    cats = opt_allowcat.strip().split()
    tarch = opt_arch if opt_arch else chroot.host_cpu()

    # collect the templates we have
    tmpls = []
    for cat in cats:
        tmpls += _collect_tmpls(None, cat)

    # collect versions into a set
    repovers = {}

    def _collect_vers(repop):
        rbase = repop / tarch
        repof = rbase / "Packages.adb"
        if not repof.is_file():
            repof = rbase / "APKINDEX.tar.gz"
        if not repof.is_file():
            return
        outp = subprocess.run(
            [
                paths.apk(),
                "--arch",
                tarch,
                "--allow-untrusted",
                "--root",
                paths.bldroot(),
                "--repository",
                str(repof),
                "search",
                "--from",
                "none",
                "-e",
                "-o",
                "-a",
            ],
            capture_output=True,
        )
        if outp.returncode != 0:
            return
        for ver in outp.stdout.strip().split():
            vers = ver.strip().decode()
            pn, pv = util.get_namever(vers)
            if pn in repovers:
                continue
            repovers[pn] = pv

    # stage versions come first
    for cat in cats:
        bpath = paths.stage_repository() / cat
        _collect_vers(bpath)
        _collect_vers(bpath / "debug")
    # actual repo
    for cat in cats:
        bpath = paths.repository() / cat
        _collect_vers(bpath)
        _collect_vers(bpath / "debug")

    vers = []
    mods = {}

    for pn in tmpls:
        tmpl = template.Template(
            pn,
            tarch,
            True,
            False,
            (1, 1),
            False,
            False,
            None,
            init=False,
            allow_restricted=opt_restricted,
        )
        mods[pn] = tmpl
        modv = tmpl._raw_mod
        # if something is wrong, mark it unbuilt, error on build later
        if (
            not hasattr(modv, "pkgname")
            or not hasattr(modv, "pkgver")
            or not hasattr(modv, "pkgrel")
        ):
            vers.append(pn)
        # get the metadata we need
        apn = getattr(modv, "pkgname")
        apv = getattr(modv, "pkgver")
        apr = getattr(modv, "pkgrel")
        if apv is None or apr is None:
            prv = ""
        else:
            prv = f"{apv}-r{apr}"
        # skip stuff that is not in repo if needed
        if outdated and apn not in repovers:
            continue
        # skip templates that are exact match
        if apn in repovers and repovers[apn] == prv:
            continue
        # otherwise build it
        vers.append(pn)

    if not vers:
        return []

    fvers = []
    tvers = {}
    tmpls = {}

    def _get_tmpl(pn):
        try:
            tmpl = mods[pn]
            tmpl.init_from_mod()
            tmpls[pn] = tmpl
            tvers[pn] = f"{tmpl.pkgver}-r{tmpl.pkgrel}"
            # sentinel
            if tmpls[pn].broken:
                tmpls[pn] = True
                return True
        except Exception:
            tmpls[pn] = False
        return False

    def _check_tmpls(pn):
        tmpl = tmpls[pn]
        # if it's unparseable, attempt it anyway (don't consider it broken)
        # alternatively it may mean we've already gone through it
        if tmpl is False:
            return False
        # if it's in repo, take the fast path (we want to keep track)
        if tmpl.pkgname in repovers:
            return False
        # else go over all the deps and check them individually
        for dpn in tmpl.get_build_deps():
            if dpn in tmpls:
                if tmpls[dpn] is True:
                    return True
            else:
                if _get_tmpl(dpn):
                    return True
            # recurse
            if _check_tmpls(dpn):
                return True
        # mark it, don't need to go over it again
        tmpls[pn] = False
        # if we're not explicitly broken anywhere, consider it
        return False

    # filter out stuff that cannot be built
    for pn in vers:
        if _get_tmpl(pn):
            continue
        fvers.append(pn)

    if not fvers:
        return []

    vers = fvers
    fvers = []

    # filter out stuff potentially not recursively buidlable
    for pn in vers:
        # recursively check for explicit brokenness
        if _check_tmpls(pn):
            continue
        fvers.append((pn, tvers[pn] if pn in tvers else None))

    return fvers


def do_update_check(tgt):
    from cbuild.core import update_check, template, chroot

    namelen = 0
    verlen = 0

    def _do_readpkg(pkgn):
        nonlocal namelen, verlen

        tmpl = template.Template(
            pkgn,
            chroot.host_cpu(),
            True,
            False,
            (1, 1),
            False,
            False,
            None,
            target="lint",
        )

        if len(tmpl.pkgver) > verlen:
            verlen = len(tmpl.pkgver)
        if len(tmpl.full_pkgname) > namelen:
            namelen = len(tmpl.full_pkgname)

        return tmpl

    def _print_upd(pn, pv, nv):
        # align name
        s = f"{pn}: "
        s += " " * (namelen - len(pn))
        # add version
        vs = f"{pv} -> {nv}"
        s += vs
        print(s)

    pkgs = []
    verbose = False

    if len(cmdline.command) < 2:
        cats = opt_allowcat.strip().split()
        # collect the templates we have
        for cat in cats:
            pkgs += _collect_tmpls(None, cat)
    else:
        pkgs.append(cmdline.command[1])
        if len(cmdline.command) > 2:
            verbose = True

    tmpls = []
    for pkg in pkgs:
        tmpls.append(_do_readpkg(pkg))

    if len(tmpls) == 1:
        cv = update_check.update_check(tmpls[0], verbose)
        for pv, nv in cv:
            _print_upd(tmpls[0].full_pkgname, pv, nv)
        return

    stmpls = sorted(
        tmpls,
        key=lambda tmpl: (
            tmpl.repository,
            tmpl.pkgname,
        ),
    )
    for tmpl in stmpls:
        cv = update_check.update_check(tmpl, verbose)
        # now we can actually print the versions
        for pv, nv in cv:
            _print_upd(tmpl.full_pkgname, pv, nv)


def do_dump(tgt):
    from cbuild.core import chroot, template, errors

    import json

    pkgn = cmdline.command[1] if len(cmdline.command) >= 2 else None

    tmpls = _collect_tmpls(pkgn)

    def _read_pkg(pkgn):
        try:
            return template.Template(
                pkgn,
                opt_arch if opt_arch else chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
        except errors.PackageException:
            return None

    dumps = []

    for tmpln in tmpls:
        pkgr = _read_pkg(tmpln)
        dumps.append(pkgr.dump())

    print(json.dumps(dumps, indent=4))


def do_print_mismatched(tgt):
    from cbuild.core import chroot, template, errors

    tmpls = _collect_tmpls(None)

    def _read_pkg(pkgn):
        try:
            return template.Template(
                pkgn,
                opt_arch if opt_arch else chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
        except errors.PackageException:
            return None

    for tmpln in tmpls:
        pkgr = _read_pkg(tmpln)
        for spkg in pkgr.subpkg_list:
            if spkg.pkgname.endswith("-default"):
                continue
            if not spkg.pkgname.startswith(f"{pkgr.pkgname}-"):
                print(f"{pkgr.pkgname} -> {spkg.pkgname}")


def do_pkg(tgt, pkgn=None, force=None, check=None, stage=None):
    from cbuild.core import build, chroot, template, errors, paths
    from cbuild.util import compiler

    if force is None:
        force = opt_force
    if check is None:
        check = opt_check
    if stage is None:
        bstage = 3
    else:
        bstage = stage
    if tgt == "invoke-custom":
        if len(cmdline.command) != 3:
            raise errors.CbuildException(f"{tgt} needs two arguments")
        tgt = "custom:" + cmdline.command[1]
        pkgn = cmdline.command[2]
    elif tgt == "pkg" and len(cmdline.command) > 2:
        return do_bulkpkg(tgt)
    elif not pkgn:
        if len(cmdline.command) <= 1 and tgt != "chroot":
            raise errors.CbuildException(f"{tgt} needs a package name")
        elif len(cmdline.command) > 2:
            raise errors.CbuildException(f"{tgt} needs only one package")
        if len(cmdline.command) > 1:
            pkgn = cmdline.command[1]
    rp = (
        template.Template(
            pkgn,
            opt_arch if opt_arch else chroot.host_cpu(),
            force,
            check,
            (opt_makejobs, opt_lthreads),
            opt_gen_dbg,
            (
                opt_ccache,
                opt_sccache,
                opt_tltocachesize if opt_tltocache else None,
            ),
            None,
            target=tgt if (tgt != "pkg") else None,
            force_check=opt_forcecheck,
            stage=bstage,
            allow_restricted=opt_restricted,
            data=opt_tdata,
        )
        if pkgn
        else None
    )
    if opt_mdirtemp:
        chroot.install()
    elif not stage:
        chroot.chroot_check()
    if tgt == "chroot":
        paths.prepare()
        chroot.shell_update(not opt_nonet, opt_dirty)
        if rp:
            rp.setup_paths()
        if rp and rp.srcdir.is_dir():
            curwrk = rp.chroot_srcdir
        elif rp and rp.srcdir.parent.is_dir():
            curwrk = rp.chroot_srcdir.parent
        else:
            curwrk = None
        chroot.enter(
            "/usr/bin/sh",
            "-i",
            fakeroot=True,
            new_session=False,
            mount_binpkgs=True,
            mount_cbuild_cache=True,
            ro_dest=False,
            env={
                "HOME": "/tmp",
                "CBUILD_SHELL": "1",
                "PS1": "\\u@\\h: \\w$ ",
                "SHELL": "/bin/sh",
            },
            wrkdir=curwrk,
            lldargs=compiler._get_lld_cpuargs(opt_lthreads),
            term=True,
        )
        return
    # don't remove builddir/destdir
    chroot.prepare_arch(opt_arch, opt_dirty)
    build.build(
        tgt,
        rp,
        {},
        dirty=opt_dirty,
        keep_temp=opt_keeptemp,
        check_fail=opt_checkfail,
        update_check=opt_updatecheck,
        accept_checksums=opt_acceptsum,
        maintainer=opt_maint,
    )
    if tgt == "pkg" and (not opt_stage or bstage < 3):
        do_unstage(tgt, bstage < 3)


def _bulkpkg(pkgs, statusf, do_build, do_raw, version):
    import graphlib

    from cbuild.core import logger, template, chroot, errors, build

    # we will use this for correct dependency ordering
    depg = graphlib.TopologicalSorter()
    templates = {}
    failed = False
    log = logger.get()

    if opt_mdirtemp:
        chroot.install()
    chroot.repo_init()
    chroot.prepare_arch(opt_arch, False)

    def _do_with_exc(f):
        # we are setting this
        nonlocal failed
        retv, fail = pkg_run_exc(f)
        if fail:
            failed = True
        return retv

    tarch = opt_arch if opt_arch else chroot.host_cpu()

    # resolve every package first
    # the result is a set of unambiguous, basic template names
    rpkgs = set()
    badpkgs = set()
    for pn in pkgs:
        # early-skip what's already handled
        if pn in rpkgs or pn in badpkgs:
            continue
        # try resolving it
        pns = template.sanitize_pkgname(pn, False)
        if not pns:
            if pns is None:
                badpkgs.add(pn)
                statusf.write(f"{pn} missing\n")
                log.out(f"\f[red]cbuild: missing package '{pn}'")
                failed = True
                continue
            else:
                badpkgs.add(pn)
                statusf.write(f"{pn} invalid\n")
                log.out(f"\f[red]cbuild: invalid package '{pn}'")
                failed = True
                continue
        # now replace with sanitized name
        npn = f"{pns.parent.name}/{pns.name}"
        # now do a second pass skip if it differs
        if npn != pn and (npn in rpkgs or npn in badpkgs):
            continue
        # skip if previously failed
        if failed and not opt_bulkcont:
            statusf.write(f"{npn} skipped\n")
            log.out(f"\f[red]cbuild: skipping template '{npn}'")
            continue
        # finally add to set
        rpkgs.add(npn)

    # visited "intermediate" templates, includes stuff that is "to be done"
    # which will be force-added after base-cbuild is handled, as we don't
    # want this to influence the graph of base-cbuild
    #
    # ignore minor errors in templates like lint as those do not concern us
    # allow broken because that does not concern us yet either (handled later)
    # do not ignore missing tmpls because that is likely error in main tmpl
    pvisit = set()

    # this is visited stuff in base-cbuild, we do checks against it later
    # to figure out if to add the implicit base-cbuild "dep" in the topology
    # as without checks we'd be creating random cycles
    cbvisit = set()

    def handle_recdeps(pn, tp, cbinit=False):
        # in raw mode we don't care about ordering, taking it as is
        if do_raw:
            return True
        # add base-cbuild "dependency" for correct implicit sorting
        if not cbinit and pn not in cbvisit and pn != "main/base-cbuild":
            depg.add(pn, "main/base-cbuild")
        # now add the rest of the stuff
        return _add_deps_graph(
            pn,
            tp,
            pvisit,
            cbvisit,
            lambda d: _do_with_exc(
                lambda: template.Template(
                    d,
                    tarch,
                    True,
                    False,
                    (1, 1),
                    False,
                    False,
                    None,
                )
            ),
            depg,
        )

    # first add base-cbuild, since that's an "implicit" dependency
    # of whatever we add in the transaction (other than cycles)
    handle_recdeps(
        "main/base-cbuild",
        template.Template(
            "main/base-cbuild",
            tarch,
            True,
            False,
            (1, 1),
            False,
            False,
            None,
        ),
        True,
    )

    # finally add the "to be done" stuff...
    for pkg in rpkgs:
        pvisit.add(pkg)

    rpkgs = sorted(rpkgs)

    # parse out all the templates first and grab their build deps
    # in raw mode, we still generate the set, we need to parse the
    # templates (but we won't be sorting it)
    for pn in rpkgs:
        # skip if previously failed and set that way
        if failed and not opt_bulkcont:
            statusf.write(f"{pn} skipped\n")
            log.out(f"\f[red]cbuild: skipping template '{pn}'")
            continue
        # parse, handle any exceptions so that we can march on
        ofailed = failed
        failed = False
        tp = _do_with_exc(
            lambda: template.Template(
                pn,
                tarch,
                opt_force,
                opt_check,
                (opt_makejobs, opt_lthreads),
                opt_gen_dbg,
                (
                    opt_ccache,
                    opt_sccache,
                    opt_tltocachesize if opt_tltocache else None,
                ),
                None,
                force_check=opt_forcecheck,
                bulk_mode=True,
                allow_restricted=opt_restricted,
                data=opt_tdata,
            )
        )
        if not tp:
            if failed:
                statusf.write(f"{pn} parse\n")
            else:
                failed = ofailed
            continue
        elif tp.broken:
            if do_build is True:
                tp.log_red(f"ERROR: {tp.broken}")
            statusf.write(f"{pn} broken\n")
            continue
        failed = False
        # add it into the graph with all its build deps
        # if some dependency in its graph fails to parse, we skip building
        # it because it could mean things building out of order (because
        # the failing template cuts the graph)
        #
        # treat dep failures the same as if it was a failure of the main
        # package, i.e., unparseable dep is like unparseable main, except
        # broken (but parseable) packages are special (and are considered
        # for the purposes of ordering)
        if not handle_recdeps(pn, tp):
            if failed:
                statusf.write(f"{pn} parse\n")
            else:
                failed = ofailed
            continue
        failed = ofailed
        # record the template for later use
        templates[pn] = tp

    flist = []
    # generate the final bulk list
    if not failed or opt_bulkcont:
        if do_raw:
            ordl = pkgs
        else:
            ordl = depg.static_order()
        # if we're raw, we iterate the input list as is
        for pn in ordl:
            # skip things that were not in the initial set
            if pn not in templates:
                continue
            tp = templates[pn]
            # if already built, mark it specially
            if not opt_force and tp.is_built(do_build is not True):
                statusf.write(f"{pn} done\n")
                continue
            if not version or tp.pkgver is None or tp.pkgrel is None:
                flist.append(pn)
            else:
                flist.append(f"{pn}={tp.pkgver}-r{tp.pkgrel}")

    if not failed or opt_bulkcont:
        if do_build is not True:
            if len(flist) > 0:
                if isinstance(do_build, list):
                    for tmpn in flist:
                        do_build.append(tmpn)
                else:
                    print(" ".join(flist))
        else:
            for pn in flist:
                tp = templates[pn]
                # if we previously failed and want it this way, skip
                if failed and not opt_bulkcont:
                    statusf.write(f"{pn} skipped\n")
                    log.out(f"\f[red]cbuild: skipping template '{pn}'")
                    continue
                # ensure to write the status
                if _do_with_exc(
                    lambda: build.build(
                        "pkg",
                        templates[pn],
                        {},
                        dirty=False,
                        keep_temp=False,
                        check_fail=opt_checkfail,
                        update_check=opt_updatecheck,
                        accept_checksums=opt_acceptsum,
                        maintainer=opt_maint,
                    )
                ):
                    statusf.write(f"{pn} ok\n")
                else:
                    statusf.write(f"{pn} failed\n")

    if failed:
        raise errors.CbuildException("at least one bulk package failed")
    elif not opt_stage and do_build is True:
        do_unstage("pkg", False)


def _collect_git(expr):
    from cbuild.core import errors, git
    import pathlib

    oexpr = expr
    # find a grep
    plus = expr.find("+")
    if plus >= 0:
        gexpr = expr[plus + 1 :]
        expr = expr[0:plus]
    else:
        gexpr = ""
    # if not a range, make it a single-commit range
    if ".." not in expr:
        expr = f"{expr}^1..{expr}"
    # make up arguments
    cmd = ["rev-list"]
    # add grep if requested
    if len(gexpr) > 0:
        nocase = gexpr.startswith("^")
        if nocase:
            gexpr = gexpr[1:]
        inv = gexpr.startswith("!")
        if inv:
            gexpr = gexpr[1:]
        if len(gexpr) > 0:
            if inv:
                cmd.append("--invert-grep")
            if nocase:
                cmd.append("--regexp-ignore-case")
            cmd.append("--grep")
            cmd.append(gexpr)
    # add commit pattern
    cmd.append(expr)
    # locate the commit list
    revs = git.call(cmd)
    if revs is None:
        raise errors.CbuildException(f"failed to resolve commits for '{oexpr}'")
    # collect changed templates
    tmpls = set()
    for commit in revs.strip().split():
        dift = git.call(
            ["diff-tree", "--no-commit-id", "--name-only", "-r", commit]
        )
        if dift is None:
            raise errors.CbuildException(
                f"failed to resolve files for '{commit.decode()}'"
            )
        for fname in dift.strip().split(b"\n"):
            fname = fname.decode()
            tn = fname.removesuffix("/template.py")
            if tn == fname or len(tn.split("/")) != 2:
                continue
            # removed packages
            if not pathlib.Path(fname).is_file():
                continue
            tmpls.add(tn)
    # and return as a list
    return list(tmpls)


def _collect_status(inf):
    pkgs = set()
    for sline in inf:
        slist = sline.split()
        if len(slist) == 0:
            continue
        elif len(slist) == 1:
            pkgs.add(slist[0])
        else:
            match slist[1]:
                case "broken" | "ok" | "invalid" | "missing":
                    continue
                case _:
                    pkgs.add(slist[0])
    # return as a list
    return list(pkgs)


def _collect_blist(pkgs):
    import sys

    rpkgs = []
    for pkg in pkgs:
        # empty args
        if not pkg:
            continue
        # git expressions
        if pkg.startswith("git:"):
            rpkgs += _collect_git(pkg.removeprefix("git:"))
            continue
        # status files
        if pkg.startswith("status:"):
            if pkg == "status:unbuilt":
                rpkgs += list(map(lambda v: v[0], _get_unbuilt()))
                continue
            if pkg == "status:outdated":
                rpkgs += list(map(lambda v: v[0], _get_unbuilt(True)))
                continue
            with open(pkg.removeprefix("status:"), "r") as inf:
                rpkgs += _collect_status(inf)
            continue
        # files
        if pkg.startswith("file:") and pkg != "file:-":
            with open(pkg.removeprefix("file:"), "r") as inf:
                for ln in inf:
                    rpkgs += _collect_blist([ln.strip()])
            continue
        # list
        if pkg.startswith("list:"):
            rpkgs += pkg[5:].split()
            continue
        # stdin
        if pkg == "-" or pkg == "file:-":
            for ln in sys.stdin:
                rpkgs += _collect_blist([ln.strip()])
            continue
        # full template name
        if "/" in pkg:
            rpkgs.append(pkg)
            continue
        # otherwise a category
        rpkgs += _collect_tmpls(None, pkg)
    # uniq it while at it
    return list(set(rpkgs))


def do_bulkpkg(tgt, do_build=True, do_raw=False, version=False):
    import os
    from cbuild.core import errors

    if do_raw:
        if len(cmdline.command) <= 1:
            raise errors.CbuildException("need at least one template")
        pkgs = cmdline.command[1:]
    elif len(cmdline.command) <= 1:
        pkgs = _collect_tmpls(None)
    else:
        pkgs = _collect_blist(cmdline.command[1:])

    if opt_statusfd:
        try:
            sout = os.fdopen(opt_statusfd, "w", 1)
        except OSError:
            raise errors.CbuildException(
                f"bad status file descriptor ({opt_statusfd})"
            )
    else:
        # fallback so we always have an object
        sout = open(os.devnull, "w")

    try:
        _bulkpkg(pkgs, sout, do_build, do_raw, version)
    except Exception:
        sout.close()
        raise


def do_prepare_upgrade(tgt):
    from cbuild.core import template, chroot, build, errors
    import pathlib

    if len(cmdline.command) < 2:
        raise errors.CbuildException("prepare-upgrade needs a package name")

    pkgn = cmdline.command[1]

    chroot.chroot_check()

    tmpl = template.Template(
        pkgn,
        opt_arch if opt_arch else chroot.host_cpu(),
        True,
        False,
        (1, 1),
        False,
        False,
        None,
        target="fetch",
        data=opt_tdata,
    )
    oldsha = list(tmpl.sha256)

    chroot.prepare_arch(opt_arch, opt_dirty)
    build.build(
        "fetch",
        tmpl,
        {},
        dirty=opt_dirty,
        keep_temp=opt_keeptemp,
        accept_checksums=True,
    )
    newsha = list(tmpl.sha256)

    tmplp = f"{tmpl.full_pkgname}/template.py"

    tmpl_source = pathlib.Path(tmplp).read_text()
    found_sha = False
    sha_replaced = set()

    with open(tmplp + ".tmp", "w") as outf:
        for ln in tmpl_source.splitlines():
            # update pkgrel
            if ln.startswith("pkgrel ="):
                outf.write("pkgrel = 0\n")
                continue
            # sha256 encountered
            if ln.strip().startswith("sha256 ="):
                found_sha = True
            elif not found_sha:
                outf.write(ln)
                outf.write("\n")
                continue
            # update checksums
            for oldck, newck in zip(oldsha, newsha):
                if oldck == newck or newck in sha_replaced:
                    continue
                nln = ln.replace(f'"{oldck}"', f'"{newck}"')
                # use new checksum once
                if ln != nln:
                    sha_replaced.add(newck)
                    ln = nln
            outf.write(ln)
            outf.write("\n")
    pathlib.Path(tmplp + ".tmp").rename(tmplp)

    tmpl.log("PACKAGE METADATA UPDATED, now verify everything is correct.")


def do_bump_pkgver(tgt):
    from cbuild.core import chroot, logger, template, errors
    from cbuild.apk import cli as acli
    import pathlib

    if len(cmdline.command) != 3:
        raise errors.CbuildException("bump-pkgver needs a name and a version")

    pkgn = cmdline.command[1]
    pkgv = cmdline.command[2]

    if not acli.check_version(pkgv):
        raise errors.CbuildException(f"version '{pkgv}' is invalid")

    try:
        tmpl = template.Template(
            pkgn,
            chroot.host_cpu(),
            True,
            False,
            (1, 1),
            False,
            False,
            None,
            target="lint",
        )
        tmplp = f"{tmpl.full_pkgname}/template.py"
        tmpl_source = pathlib.Path(tmplp).read_text()
        with open(tmplp + ".tmp", "w") as outf:
            for ln in tmpl_source.splitlines():
                # update pkgver
                if ln.startswith("pkgver ="):
                    outf.write(f'pkgver = "{pkgv}"\n')
                    continue
                # reset pkgrel to zero
                if ln.startswith("pkgrel ="):
                    outf.write("pkgrel = 0\n")
                    continue
                outf.write(ln)
                outf.write("\n")
        pathlib.Path(tmplp + ".tmp").rename(tmplp)
        logger.get().out(f"Updated version: {pkgn} {tmpl.pkgver} => {pkgv}")
    except Exception:
        logger.get().out(f"\f[orange]WARNING: Failed to update version: {pkgn}")


def do_bump_pkgrel(tgt):
    from cbuild.core import chroot, logger, template, errors
    import pathlib

    if len(cmdline.command) < 2:
        raise errors.CbuildException("bump-pkgrel needs at least one name")

    for pkgn in cmdline.command[1:]:
        try:
            tmpl = template.Template(
                pkgn,
                chroot.host_cpu(),
                True,
                False,
                (1, 1),
                False,
                False,
                None,
                target="lint",
            )
            pr = tmpl.pkgrel
            tmplp = f"{tmpl.full_pkgname}/template.py"
            tmpl_source = pathlib.Path(tmplp).read_text()
            with open(tmplp + ".tmp", "w") as outf:
                for ln in tmpl_source.splitlines():
                    # update pkgrel
                    if ln.startswith("pkgrel ="):
                        outf.write(f"pkgrel = {pr + 1}\n")
                        continue
                    outf.write(ln)
                    outf.write("\n")
            pathlib.Path(tmplp + ".tmp").rename(tmplp)
            logger.get().out(f"Bumped pkgrel: {pkgn}")
        except Exception:
            logger.get().out(
                f"\f[orange]WARNING: Failed to bump pkgrel: {pkgn}"
            )


class InteractiveCompleter:
    def complete(self, text, state):
        import pathlib
        import readline
        import shlex

        if state == 0:
            self.matches = []
            lbuf = readline.get_line_buffer()
            lbeg = readline.get_begidx()
            lend = readline.get_endidx()
            ptext = lbuf[0:lbeg]
            ctext = lbuf[lbeg:lend]
            # previously matched a category, so match a template now
            if ptext.endswith("/"):
                pcat = shlex.split(ptext)[-1][0:-1]
                for cat in opt_allowcat.split():
                    if cat == pcat:
                        break
                else:
                    # no category match
                    return None
                # matched category so try to find a template
                cp = pathlib.Path(pcat)
                if not cp.is_dir():
                    return None
                if "*" not in text:
                    text += "*"
                for gl in cp.glob(text):
                    if gl.is_symlink() or not gl.is_dir():
                        continue
                    self.matches.append(gl.name)
            else:
                if "alias" in global_cfg:
                    alias_map = global_cfg["alias"]
                else:
                    alias_map = None
                carr = shlex.split(lbuf)
                if len(carr) == 0:
                    ctext = ""
                else:
                    ctext = carr[-1]
                for v in command_handlers:
                    if not ctext or v.startswith(ctext):
                        self.matches.append(v.removeprefix(ptext))
                for v in alias_map:
                    if not ctext or v.startswith(ctext):
                        self.matches.append(v.removeprefix(ptext))
                for v in opt_allowcat.split():
                    if not ctext or v.startswith(ctext):
                        self.matches.append(v.removeprefix(ptext) + "/")
                self.matches.sort()
        try:
            return self.matches[state]
        except IndexError:
            pass
        return None


def do_commit(tgt):
    from cbuild.core import errors, chroot, paths, template, logger, git
    import tempfile
    import os

    # filter the args for valid templates
    copts = []
    tmpls = []
    try_all = False

    for cmd in cmdline.command[1:]:
        if cmd.startswith("-"):
            copts.append(cmd)
        elif cmd == "all":
            try_all = True
        else:
            tmpls.append(cmd)

    # collect files known to git...
    gits = git.call(["status", "--porcelain"])
    if gits is None:
        raise errors.CbuildException("failed to resolve git changes")

    # mew mew
    cats = list(map(lambda v: f"{v}/", opt_allowcat.strip().split()))

    chtmpls = {}

    # track changes in a set so we know what we can pass to commit
    changes = set()
    for ln in gits.splitlines():
        ln = ln.strip().split(b" ", 1)
        if len(ln) != 2:
            continue
        chng = ln[1].decode()
        for cat in cats:
            if not chng.startswith(cat):
                continue
            tmpn = cat + chng.removeprefix(cat).split("/")[0]
            if template.sanitize_pkgname(tmpn, False):
                if tmpn not in chtmpls or not chtmpls[tmpn]:
                    chtmpls[tmpn] = ln[0] == b"M"
            break
        changes.add(chng)

    if len(tmpls) < 1:
        # just print changed status
        log = logger.get()
        if len(chtmpls) == 0:
            log.out("No templates changed.")
            return
        if try_all:
            tmpls = list(chtmpls)
        else:
            log.out("Changed templates:")
            for tmp in sorted(chtmpls):
                log.out(
                    f"  \f[{'green' if not chtmpls[tmp] else 'orange'}]* {tmp}"
                )
            return

    hcpu = chroot.host_cpu()

    def build_tmpl(sname, contents):
        return template.Template(
            sname,
            hcpu,
            True,
            False,
            (1, 1),
            False,
            False,
            None,
            target="lint",
            contents=contents,
        )

    # parse everything first so we know stuff's intact, store before calling git
    tmplos = []

    for tmp in tmpls:
        # we don't handle template deletion yet... maybe sometime
        sname = template.sanitize_pkgname(tmp)
        # try getting the HEAD contents of it
        relh = str(sname.relative_to(paths.distdir()) / "template.py")
        head = git.call(["show", f"HEAD:{relh}"])
        # try building a template object of the old state
        if head is not None:
            try:
                otmpl = build_tmpl(sname, head.decode())
            except Exception:
                # differentiate failure to parse and non-existence
                otmpl = None
        else:
            otmpl = False
        # build the current contents of it, this has to succeed
        tmpl = build_tmpl(sname, None)
        tfiles = {tmpl.full_pkgname}
        # store
        tmplos.append((tmpl, otmpl, tfiles))

    ddir = paths.distdir()

    # for each template pair, recreate subpackage symlinks
    for tmpl, otmpl, tfiles in tmplos:
        if otmpl:
            # remove potentially old subpkg symlinks
            for osp in otmpl.subpkg_list:
                p = ddir / otmpl.repository / osp.pkgname
                if not p.exists():
                    continue
                p.unlink()
                tf = f"{otmpl.repository}/{osp.pkgname}"
                tfiles.add(tf)
                changes.add(tf)
        # create new subpkg symlinks
        for sp in tmpl.subpkg_list:
            p = ddir / tmpl.repository / sp.pkgname
            p.unlink(missing_ok=True)
            p.symlink_to(tmpl.pkgname)
            tf = f"{tmpl.repository}/{sp.pkgname}"
            tfiles.add(tf)
            changes.add(tf)

    # commit in topologically sorted order where possible, for that
    # we need a sorted list of templates (reuse the bulk build code)
    itmpls = list(map(lambda v: v[0].full_pkgname, tmplos))
    stmpls = []
    sout = open(os.devnull, "w")
    _bulkpkg(itmpls, sout, stmpls, False, False)

    bulkset = set(stmpls)
    bulkmap = {}

    for tmpl, otmpl, tfiles in tmplos:
        if tmpl.full_pkgname not in bulkset:
            # put unsortable stuff at the end
            stmpls.append(tmpl.full_pkgname)
        # for later lookup
        bulkmap[tmpl.full_pkgname] = (tmpl, otmpl, tfiles)

    # now for each, run git commit...
    for tmpln in stmpls:
        tmpl, otmpls, tfiles = bulkmap[tmpln]
        if otmpl is False:
            # new package
            msg = f"{tmpl.full_pkgname}: new package"
        elif not otmpl:
            # previously failed to parse (fix?)
            msg = f"{tmpl.full_pkgname}: fix [reason here]"
        elif otmpl.pkgver != tmpl.pkgver:
            # new version
            msg = f"{tmpl.full_pkgname}: update to {tmpl.pkgver}"
        elif otmpl.pkgrel != tmpl.pkgrel:
            # revision bump
            msg = f"{tmpl.full_pkgname}: rebuild for [reason here]"
        else:
            # other change
            msg = f"{tmpl.full_pkgname}: [description here]"
        # now fill in the rest, build list
        xl = sorted(tfiles)
        # make all the files known to git, but don't add them
        git.call(["add", "-N", *xl])
        # and run it
        with tempfile.NamedTemporaryFile("w", delete_on_close=False) as nf:
            nf.write(msg)
            nf.write("\n")
            nf.close()
            # allow-empty-message because git is silly and complains if you do not edit
            git.call(
                [
                    "commit",
                    "--allow-empty-message",
                    "-t",
                    nf.name,
                    *copts,
                    *xl,
                ],
                foreground=True,
                gitconfig=True,
            )


def do_interactive(tgt):
    import os
    import shlex
    import readline

    from cbuild.core import logger

    global cmdline

    readline.set_completer(InteractiveCompleter().complete)
    # default is something like ' \t\n`~!@#$%^&*()-=+[{]}\\|;:\'",<>/?'
    readline.set_completer_delims(" \t\n/")

    bkend = "readline"
    try:
        bkend = readline.backend
    except AttributeError:
        if readline._READLINE_LIBRARY_VERSION.startswith("EditLine"):
            bkend = "editline"

    if bkend == "readline":
        readline.parse_and_bind("set editing-mode vi")
    elif bkend == "editline":
        readline.parse_and_bind("python:bind -v")

    readline.set_history_length(1000)

    try:
        if os.path.exists("etc/inputrc"):
            readline.read_init_file("etc/inputrc")
        else:
            readline.read_init_file()
    except OSError:
        pass

    if bkend == "readline":
        readline.parse_and_bind("tab: complete")
    elif bkend == "editline":
        readline.parse_and_bind("python:bind ^I rl_complete")

    while True:
        pmpt = shlex.split(input("cbuild> "))
        try:
            cmdline = parser.parse_intermixed_args(pmpt)
        except SystemExit:
            logger.get().out("\f[red]cbuild: invalid command line")
            continue
        fire_cmd()


#
# MAIN ENTRYPOINT
#

command_handlers = {
    "binary-bootstrap": (
        binary_bootstrap,
        "Set up the build container (alias for bootstrap)",
    ),
    "bootstrap": (binary_bootstrap, "Bootstrap the build container"),
    "bootstrap-update": (bootstrap_update, "Update the build container"),
    "build": (do_pkg, "Run up to build phase of a template"),
    "bulk-pkg": (do_bulkpkg, "Perform a bulk build"),
    "bulk-print": (
        lambda cmd: do_bulkpkg(cmd, False),
        "Print a bulk build list",
    ),
    "bulk-print-ver": (
        lambda cmd: do_bulkpkg(cmd, False, version=True),
        "Print a bulk build list with versions",
    ),
    "bulk-raw": (
        lambda cmd: do_bulkpkg(cmd, True, True),
        "Perform an unsorted bulk build",
    ),
    "bump-pkgrel": (do_bump_pkgrel, "Increase the pkgrel of a template"),
    "bump-pkgver": (do_bump_pkgver, "Update the pkgver of a template"),
    "check": (do_pkg, "Run up to check phase of a template"),
    "chroot": (do_pkg, "Enter an interactive bldroot chroot"),
    "clean": (do_clean, "Clean the build directory"),
    "commit": (do_commit, "Commit the changes in the template"),
    "configure": (do_pkg, "Run up to configure phase of a template"),
    "cycle-check": (
        do_cycle_check,
        "Perform a depcycle check on all templates",
    ),
    "deps": (do_pkg, "Run up to the deps installation phase of a template"),
    "dump": (do_dump, "Dump the metadata of all templates to the terminal"),
    "fetch": (do_pkg, "Run up to fetch phase of a template"),
    "extract": (do_pkg, "Run up to extract phase of a template"),
    "index": (do_index, "Reindex local repositories"),
    "install": (do_pkg, "Run up to install phase of a template"),
    "invoke-custom": (do_pkg, "Run a custom template-specific target"),
    "keygen": (do_keygen, "Generate a new signing key"),
    "lint": (do_lint, "Parse a template and lint it"),
    "patch": (do_pkg, "Run up to patch phase of a template"),
    "pkg": (do_pkg, "Build a package or multiple packages"),
    "prepare": (do_pkg, "Run up to prepare phase of a template"),
    "prepare-upgrade": (
        do_prepare_upgrade,
        "Update template checksums and reset pkgrel",
    ),
    "print-build-graph": (
        do_print_build_graph,
        "Print the build graph of a template",
    ),
    "print-mismatched-subpkgs": (
        do_print_mismatched,
        "Print subpackages that have wrong names",
    ),
    "prune-pkgs": (
        do_prune_pkgs,
        "Prune obsolete and removed packages from local repos",
    ),
    "prune-obsolete": (
        do_prune_obsolete,
        "Prune obsolete packages from local repos",
    ),
    "prune-removed": (
        do_prune_removed,
        "Prune removed packages from local repos",
    ),
    "prune-sources": (do_prune_sources, "Prune local sources"),
    "relink-subpkgs": (do_relink_subpkgs, "Remake subpackage symlinks"),
    "remove-autodeps": (
        do_remove_autodeps,
        "Remove build dependencies from bldroot",
    ),
    "source-bootstrap": (
        bootstrap,
        "Bootstrap the build container from scratch",
    ),
    "unstage": (
        lambda cmd: do_unstage(cmd, opt_force),
        "Unstage local repositories",
    ),
    "unstage-check-remote": (
        check_unstage,
        "Try unstaging local packages against remote repositories",
    ),
    "update-check": (do_update_check, "Check a template for upstream updates"),
    "zap": (do_zap, "Remove the bldroot"),
    "interactive": (do_interactive, "Enter interactive prompt"),
}


def fire_cmd():
    import shutil
    import sys

    from cbuild.core import logger, paths

    retcode = None

    if "alias" in global_cfg:
        alias_map = global_cfg["alias"]
    else:
        alias_map = None

    def bodyf():
        nonlocal retcode
        cmd = cmdline.command[0]
        if "/" in cmd and len(cmdline.command) >= 2:
            # allow reverse order for commands taking package names
            ncmd = cmdline.command[1]
            cmdline.command[0] = ncmd
            cmdline.command[1] = cmd
            cmd = ncmd
        # if aliased, get the rel name
        if alias_map:
            cmd = alias_map.get(cmd, fallback=cmd)
        if cmd in command_handlers:
            retcode = command_handlers[cmd][0](cmd)
        else:
            logger.get().out(f"\f[red]cbuild: invalid target {cmd}")
            sys.exit(1)
        return None

    ret, failed = pkg_run_exc(bodyf)

    if opt_mdirtemp and not opt_keeptemp:
        shutil.rmtree(paths.bldroot())

    return ret, failed, retcode


def fire():
    import sys
    import subprocess

    from cbuild.core import build, chroot, logger, template, profile
    from cbuild.core import paths
    from cbuild.apk import cli
    from cbuild.util import flock

    logger.init(not opt_nocolor, opt_timing)
    flock.set_nolock(opt_nolock)

    # set host arch to provide early guarantees
    if opt_harch:
        chroot.set_host(opt_harch)
    else:
        chroot.set_host(cli.get_arch())

    # check container and while at it perform arch checks
    chroot.chroot_check(error=False)

    # register extra packages
    chroot.set_extras(opt_epkgs.split())

    # set the repo mirror
    chroot.set_mirror(opt_apkrepo)

    # set depcheck
    chroot.set_depcheck(not opt_nodepcheck)

    # ensure we've got a signing key
    if not opt_signkey and cmdline.command[0] != "keygen":
        logger.get().out("\f[red]cbuild: no signing key set")
        sys.exit(1)

    # initialize profiles
    profile.init(global_cfg)

    # check target arch validity if provided
    if opt_arch:
        try:
            profile.get_profile(opt_arch)
        except Exception:
            logger.get().out(
                f"\f[red]cbuild: unknown target architecture '{opt_arch}'"
            )
            sys.exit(1)
    # let apk know if we're using network
    cli.set_network(not opt_nonet)

    try:
        aret = subprocess.run([paths.apk(), "--version"], capture_output=True)
    except FileNotFoundError:
        logger.get().out(
            f"\f[red]cbuild: apk not found (expected path: {paths.apk()})"
        )
        sys.exit(1)

    if not aret.stdout.startswith(b"apk-tools 3"):
        logger.get().out("\f[red]cbuild: apk-tools 3.x is required")
        sys.exit(1)

    try:
        subprocess.run([paths.bwrap(), "--version"], capture_output=True)
    except FileNotFoundError:
        logger.get().out(
            f"\f[red]cbuild: bwrap not found (expected path: {paths.bwrap()})"
        )
        sys.exit(1)

    build.register_hooks()
    template.register_cats(opt_allowcat.strip().split())

    ret, failed, retcode = fire_cmd()

    if failed:
        sys.exit(1)
    elif retcode:
        sys.exit(retcode)
