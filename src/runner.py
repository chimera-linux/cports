#!/usr/bin/env python3

cbpath = None
rtpath = None

# global options

global_cfg = None
cmdline = None

opt_apkcmd     = "apk"
opt_cflags     = "-O2"
opt_cxxflags   = "-O2"
opt_fflags     = "-O2"
opt_arch       = None
opt_gen_dbg    = True
opt_check      = True
opt_ccache     = False
opt_makejobs   = 0
opt_nocolor    = False
opt_signkey    = None
opt_unsigned   = False
opt_force      = False
opt_mdirtemp   = False
opt_nonet      = False
opt_dirty      = False
opt_keeptemp   = False
opt_forcecheck = False
opt_checkfail  = False
opt_stage      = False
opt_dryrun     = False
opt_altrepo    = None
opt_bldroot    = "bldroot"
opt_pkgpath    = "packages"
opt_srcpath    = "sources"
opt_cchpath    = "cbuild_cache"
opt_statusfd   = None
opt_bulkfail   = False

#
# INITIALIZATION ROUTINES
#

def init_early():
    import os
    import sys
    import signal

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
    import argparse
    import pathlib
    import tempfile
    import configparser

    global global_cfg
    global cmdline

    global opt_apkcmd, opt_dryrun, opt_bulkfail
    global opt_cflags, opt_cxxflags, opt_fflags
    global opt_arch, opt_gen_dbg, opt_check, opt_ccache
    global opt_makejobs, opt_nocolor, opt_signkey, opt_unsigned
    global opt_force, opt_mdirtemp, opt_nonet, opt_dirty, opt_statusfd
    global opt_keeptemp, opt_forcecheck, opt_checkfail, opt_stage, opt_altrepo
    global opt_bldroot, opt_pkgpath, opt_srcpath, opt_cchpath

    # respect NO_COLOR
    opt_nocolor = ("NO_COLOR" in os.environ) or not sys.stdout.isatty()

    parser = argparse.ArgumentParser(
        description = "Chimera Linux build system."
    )

    parser.add_argument(
        "-c", "--config", default = "etc/config.ini",
        help = "The configuration file to use."
    )
    parser.add_argument(
        "-f", "--force", action = "store_const", const = True,
        default = opt_force,
        help = "Force writing a package even when it exists and template is older."
    )
    parser.add_argument(
        "-L", "--no-color", action = "store_const", const = True,
        default = opt_nocolor, help = "Force plain output."
    )
    parser.add_argument(
        "-j", "--jobs", help = "Number of jobs to use.", default = None
    )
    parser.add_argument(
        "-C", "--skip-check", action = "store_const",
        const = True, default = not opt_check,
        help = "Skip running the check stage."
    )
    parser.add_argument(
        "--force-check", action = "store_const",
        const = True, default = opt_forcecheck,
        help = "Force running check even if disabled by template."
    )
    parser.add_argument(
        "-X", "--check-fail", action = "store_const",
        const = True, default = opt_checkfail,
        help = "Do not abort build if check fails."
    )
    parser.add_argument(
        "-G", "--no-dbg", action = "store_const",
        const = True, default = not opt_gen_dbg,
        help = "Do not build debug packages."
    )
    parser.add_argument(
        "-a", "--arch", help = "Target architecture to build for.",
        default = None
    )
    parser.add_argument(
        "-b", "--build-root", default = None, help = "The build root path."
    )
    parser.add_argument(
        "-r", "--repository-path", default = None,
        help = "Local repository path."
    )
    parser.add_argument(
        "-R", "--alt-repository", default = None,
        help = "Alternative repository to use."
    )
    parser.add_argument(
        "-s", "--sources-path", default = None,
        help = "Sources storage path."
    )
    parser.add_argument(
        "-t", "--temporary", action = "store_const",
        const = True, default = opt_mdirtemp,
        help = "Use a temporary build root."
    )
    parser.add_argument(
        "-N", "--no-remote", action = "store_const",
        const = True, default = opt_nonet,
        help = "Do not ever use remote repositories."
    )
    parser.add_argument(
        "-D", "--dirty-build", action = "store_const",
        const = True, default = opt_dirty,
        help = "Skip installing (and removing) dependencies."
    )
    parser.add_argument(
        "-K", "--keep-temporary", action = "store_const",
        const = True, default = opt_keeptemp,
        help = "Keep temporary files and build dependencies after build."
    )
    parser.add_argument(
        "--allow-unsigned", action = "store_const",
        const = True, default = opt_unsigned,
        help = "Allow building without a signing key."
    )
    parser.add_argument(
        "--stage", action = "store_const",
        const = True, default = opt_stage,
        help = "Keep built packages staged."
    )
    parser.add_argument(
        "--dry-run", action = "store_const",
        const = True, default = opt_dryrun,
        help = "Do not perform changes to file system (only some commands)"
    )
    parser.add_argument(
        "--status-fd", default = None,
        help = "File descriptor for bulk build status (must be open)."
    )
    parser.add_argument(
        "--bulk-fail", action = "store_const",
        const = True, default = opt_bulkfail,
        help = "Skip remaining packages after first failure for bulk builds."
    )
    parser.add_argument("command", nargs = "+", help = "The command to issue.")

    cmdline = parser.parse_args()

    # parse config file and set the global options from it

    global_cfg = configparser.ConfigParser()
    global_cfg.read(cmdline.config)

    if "apk" in global_cfg:
        apkcfg = global_cfg["apk"]

        opt_apkcmd = apkcfg.get("command", fallback = opt_apkcmd)

    if "build" in global_cfg:
        bcfg = global_cfg["build"]

        opt_gen_dbg   = bcfg.getboolean("build_dbg", fallback = opt_gen_dbg)
        opt_ccache    = bcfg.getboolean("ccache", fallback = opt_ccache)
        opt_check     = bcfg.getboolean("check", fallback = opt_check)
        opt_checkfail = bcfg.getboolean("check_fail", fallback = opt_checkfail)
        opt_stage     = bcfg.getboolean("keep_stage", fallback = opt_stage)
        opt_makejobs  = bcfg.getint("jobs", fallback = opt_makejobs)
        opt_arch      = bcfg.get("arch", fallback = opt_arch)
        opt_bldroot   = bcfg.get("build_root", fallback = opt_bldroot)
        opt_altrepo   = bcfg.get("alt_repository", fallback = opt_altrepo)
        opt_pkgpath   = bcfg.get("repository", fallback = opt_pkgpath)
        opt_srcpath   = bcfg.get("sources", fallback = opt_srcpath)
        opt_cchpath   = bcfg.get("cbuild_cache_path", fallback = opt_cchpath)

    if not "flags" in global_cfg:
        global_cfg["flags"] = {}

    if not "CFLAGS" in global_cfg["flags"]:
        global_cfg["flags"]["CFLAGS"] = opt_cflags

    if not "CXXFLAGS" in global_cfg["flags"]:
        global_cfg["flags"]["CXXFLAGS"] = opt_cxxflags

    if not "FFLAGS" in global_cfg["flags"]:
        global_cfg["flags"]["FFLAGS"] = opt_fflags

    if "signing" in global_cfg:
        signcfg = global_cfg["signing"]

        opt_signkey = signcfg.get("key", fallback = opt_signkey)

    # command line args override config file

    if cmdline.jobs:
        opt_makejobs = int(cmdline.jobs)

    if cmdline.no_dbg:
        opt_gen_dbg = False

    if cmdline.arch:
        opt_arch = cmdline.arch

    if cmdline.no_color:
        opt_nocolor = True

    if cmdline.force:
        opt_force = True

    if cmdline.skip_check:
        opt_check = False

    if cmdline.build_root:
        opt_bldroot = cmdline.build_root

    if cmdline.repository_path:
        opt_pkgpath = cmdline.repository_path

    if cmdline.alt_repository:
        opt_altrepo = cmdline.alt_repository

    if cmdline.sources_path:
        opt_srcpath = cmdline.sources_path

    if cmdline.no_remote:
        opt_nonet = True

    if cmdline.dirty_build:
        opt_dirty = True

    if cmdline.keep_temporary:
        opt_keeptemp = True

    if cmdline.force_check:
        opt_forcecheck = True

    if cmdline.check_fail:
        opt_checkfail = True

    if cmdline.temporary:
        mdp = pathlib.Path.cwd() / opt_bldroot
        # the temporary directory should be in the same location as build root
        opt_mdirtemp = True
        opt_bldroot  = tempfile.mkdtemp(
            prefix = mdp.name + ".", dir = mdp.parent
        )

    if cmdline.stage:
        opt_stage = True

    if cmdline.dry_run:
        opt_dryrun = True

    if cmdline.status_fd:
        opt_statusfd = int(cmdline.status_fd)

    if cmdline.bulk_fail:
        opt_bulkfail = True

    if opt_makejobs == 0:
        opt_makejobs = len(os.sched_getaffinity(0))

def init_late():
    import os

    from cbuild.core import paths, spdx

    mainrepo = opt_altrepo
    altrepo = opt_pkgpath
    if not mainrepo:
        mainrepo = opt_pkgpath
        altrepo = None

    # init paths early, modules rely on it
    paths.init(
        cbpath, rtpath, opt_bldroot, mainrepo, altrepo, opt_srcpath,
        opt_cchpath
    )

    # apk command
    if "CBUILD_APK_PATH" in os.environ:
        paths.set_apk(os.environ["CBUILD_APK_PATH"])
    else:
        paths.set_apk(opt_apkcmd)

    # init license information
    spdx.init()

#
# ACTIONS
#

def binary_bootstrap(tgt):
    from cbuild.core import chroot, paths

    paths.prepare()

    if len(cmdline.command) <= 1:
        chroot.install(chroot.host_cpu())
    else:
        chroot.install(cmdline.command[1])

def do_unstage(tgt, force = False):
    from cbuild.core import chroot, stage

    if opt_arch and opt_arch != chroot.host_cpu():
        stage.clear(opt_arch, opt_signkey, force)

    stage.clear(chroot.host_cpu(), opt_signkey, force)

def bootstrap(tgt):
    import sys
    import shutil

    from cbuild.core import build, chroot, logger, template, paths

    max_stage = 2

    if len(cmdline.command) > 1:
        max_stage = int(cmdline.command[1])

    oldmdir = paths.bldroot()

    paths.set_stage(0)
    paths.reinit_buildroot(oldmdir, 0)

    if not chroot.chroot_check(True):
        logger.get().out("cbuild: bootstrapping stage 0")

        # extra program checks
        for prog in [
            "clang", "lld", "cmake", "meson", "patch", "pkg-config",
            "make", "ninja", "strip", "byacc", "flex", "perl", "m4"
        ]:
            if not shutil.which(prog):
                sys.exit(f"Required bootstrap program not found: {prog}")

        if not shutil.which("gmake") and not shutil.which("bmake"):
            sys.exit("Required bootstrap program not found: gmake/bmake")

        rp = None
        try:
            rp = template.read_pkg(
                "main/base-cbuild", None, False, False, opt_makejobs,
                False, False, None, stage = 0
            )
        except template.SkipPackage:
            pass
        paths.prepare()
        chroot.initdb()
        chroot.repo_sync()
        if rp:
            build.build(tgt, rp, {}, opt_signkey)
        do_unstage(tgt, True)
        shutil.rmtree(paths.bldroot())
        chroot.install(chroot.host_cpu())

    if max_stage == 0:
        return

    # change binary repo path
    paths.set_stage(1)
    # set build root to stage 1 for chroot check
    paths.reinit_buildroot(oldmdir, 1)

    if not chroot.chroot_check(True):
        logger.get().out("cbuild: bootstrapping stage 1")
        # use stage 0 build root to build, but build into stage 1 repo
        paths.reinit_buildroot(oldmdir, 0)
        try:
            do_pkg("pkg", "main/base-cbuild", False, False, stage = 1)
        except template.SkipPackage:
            pass
        # go back to stage 1
        paths.reinit_buildroot(oldmdir, 1)
        chroot.install(chroot.host_cpu())

    if max_stage == 1:
        return

    # change binary repo path
    paths.set_stage(2)
    # set build root to stage 2 for chroot check
    paths.reinit_buildroot(oldmdir, 2)

    if not chroot.chroot_check(True):
        logger.get().out("cbuild: bootstrapping stage 2")
        # use stage 1 build root to build, but build into stage 2 repo
        paths.reinit_buildroot(oldmdir, 1)
        try:
            do_pkg("pkg", "main/base-cbuild", False, False, stage = 2)
        except template.SkipPackage:
            pass
        # go back to stage 2
        paths.reinit_buildroot(oldmdir, 2)
        chroot.install(chroot.host_cpu())

    # change binary repo path
    paths.set_stage(3)
    # set build root to stage 3 for chroot check
    paths.reinit_buildroot(oldmdir, 3)

    if not chroot.chroot_check(True):
        logger.get().out("cbuild: bootstrapping stage 3")
        # use stage 1 build root to build, but build into stage 2 repo
        paths.reinit_buildroot(oldmdir, 2)
        try:
            do_pkg("pkg", "main/base-cbuild", False)
        except template.SkipPackage:
            pass
        # go back to stage 3
        paths.reinit_buildroot(oldmdir, 3)
        chroot.install(chroot.host_cpu())

def bootstrap_update(tgt):
    from cbuild.core import chroot

    chroot.remove_autodeps(False)
    chroot.update()

def do_keygen(tgt):
    from cbuild.apk import sign

    if len(cmdline.command) >= 3:
        keyn, keysize = cmdline.command[1], int(cmdline.command[2])
    elif len(cmdline.command) >= 2:
        keyn, keysize = cmdline.command[1], 2048
    else:
        keyn, keysize = None, 2048

    if not keyn or len(keyn) == 0:
        keyn = opt_signkey

    sign.keygen(keyn, keysize, global_cfg, cmdline.config)

def do_chroot(tgt):
    from cbuild.core import chroot, paths

    if opt_mdirtemp:
        chroot.install(chroot.host_cpu())
    paths.prepare()
    chroot.repo_sync(True)
    chroot.enter(
        "/usr/bin/mksh.static", "-i", fakeroot = True, new_session = False,
        mount_binpkgs = True, mount_cbuild_cache = True,
        env = {
            "HOME": "/tmp",
            "TERM": "linux",
            "CBUILD_SHELL": "1",
            "PS1": "$PWD$ ",
            "SHELL": "/usr/bin/mksh.static",
        }
    )

def do_clean(tgt):
    import shutil

    from cbuild.core import chroot, logger, paths

    chroot.remove_autodeps(None)
    dirp = paths.bldroot() / "builddir"
    if dirp.is_dir():
        shutil.rmtree(dirp)
    elif dirp.exists():
        raise errors.CbuildException("broken container (builddir invalid)")
    dirp = paths.bldroot() / "destdir"
    if dirp.is_dir():
        shutil.rmtree(dirp)
    elif dirp.exists():
        raise errors.CbuildException("broken container (destdir invalid)")

def do_zap(tgt):
    import shutil

    from cbuild.core import logger, paths

    if paths.bldroot().is_dir():
        shutil.rmtree(paths.bldroot())
    elif paths.bldroot().exists():
        raise errors.CbuildException("broken build container")

def do_remove_autodeps(tgt):
    from cbuild.core import chroot

    chroot.remove_autodeps(None)

def do_prune_obsolete(tgt):
    from cbuild.core import chroot, logger, paths
    from cbuild.apk import cli

    logger.get().out("cbuild: pruning repositories...")
    # ensure we know what cpu arch we are dealing with
    chroot.chroot_check()

    reposd = paths.repository()
    reposet = {}

    for idx in reposd.rglob("APKINDEX.tar.gz"):
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

    from cbuild.core import chroot, logger, paths, template
    from cbuild.apk import cli

    # ensure we know what cpu arch we are dealing with
    chroot.chroot_check()
    # FIXME: compute from git if possible
    epoch = int(time.time())
    # do specific arch only
    archn = opt_arch
    if not archn:
        archn = chroot.target_cpu()
    # pruner for a single repo
    def _prune(repo):
        logger.get().out(f"Pruning removed packages at '{repo}'...")
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
        for pkg in (repo / archn).glob("*.apk"):
            pkgn = pkg.stem
            rd = pkgn.rfind("-")
            if rd > 0:
                rd = pkgn.rfind("-", 0, rd)
            if rd < 0:
                logger.get().warn(
                    f"Malformed file name found, skipping: {pkg.name}"
                )
                continue
            pkgn = pkgn[0:rd]
            # automatic subpackages are special, except when explicit
            opkgn = pkgn
            if not (tmplp / pkgn).exists():
                for apkg, adesc, iif, takef in template.autopkgs:
                    if pkgn.endswith(f"-{apkg}"):
                        pkgn = pkgn[:-len(apkg) - 1]
                        break
            # if it's ok, just skip
            if (tmplp / pkgn).exists():
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
                logger.get().warn(
                    f"Broken symlink for package '{pkgn}'"
                )
            logger.get().out(f"Pruning package: {pkg.name}")
            if not opt_dryrun:
                pkg.unlink()
        # reindex
        if not opt_dryrun:
            cli.build_index(repo / archn, epoch, opt_signkey)

    reposd = paths.repository()
    reposet = {}
    # find all existing indexes
    for idx in reposd.rglob("APKINDEX.tar.gz"):
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

def do_index(tgt):
    import time
    import pathlib

    from cbuild.core import chroot, logger, paths
    from cbuild.apk import cli

    idir = cmdline.command[1] if len(cmdline.command) >= 2 else None
    # ensure we know what cpu arch we are dealing with
    chroot.chroot_check()
    # FIXME: compute from git if possible
    epoch = int(time.time())
    # do specific arch only
    archn = opt_arch
    if not archn:
        archn = chroot.target_cpu()
    # indexer for a single repo
    def _index(repo):
        logger.get().out(f"Indexing packages at '{repo}'...")
        cli.build_index(repo / archn, epoch, opt_signkey)
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
    for idx in reposd.rglob("APKINDEX.tar.gz"):
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
    template.read_pkg(
        pkgn, opt_arch if opt_arch else chroot.host_cpu(), True,
        False, 1, False, False, None, target = "lint"
    )

def _collect_tmpls(pkgn):
    from cbuild.core import paths

    tmpls = []

    if pkgn:
        tmpls.append(pkgn)
    else:
        for cat in paths.distdir().iterdir():
            if cat.is_symlink() or not cat.is_dir():
                continue
            for tmpl in cat.iterdir():
                if tmpl.is_symlink() or not tmpl.is_dir():
                    continue
                pathf = tmpl / "template.py"
                if pathf.exists() and pathf.is_file():
                    tmpls.append(f"{cat.name}/{tmpl.name}")

    tmpls.sort()

    return tmpls

def do_cycle_check(tgt):
    from cbuild.core import dependencies, chroot, logger, template, paths
    from cbuild.apk import util as autil

    pkgn = cmdline.command[1] if len(cmdline.command) >= 2 else None

    # broken packages get removed from testing
    def _read_pkg(pkgn, resolve):
        try:
            return template.read_pkg(
                pkgn, chroot.host_cpu(), True,
                False, 1, False, False, None, target = "lint",
                resolve = resolve, allow_broken = True,
                ignore_errors = True
            )
        except PackageError:
            return None

    # template list, one template or all
    tmpls = _collect_tmpls(pkgn)
    # saved cycle path for informational purposes
    curpath = []
    # this saves all already-tested templates so we can skip them
    tested = {}
    # templates encountered during the current run
    encountered = {}
    # skip known already-printed cycles
    cycled = {}

    def _cycle_check(tmpln, ppkg):
        bpkgn = tmpln
        pkgs = bpkgn.find("/")
        if pkgs > 0:
            bpkgn = bpkgn[pkgs + 1:]
        nonlocal curpath
        # skip if the cycle is already known
        if bpkgn in cycled:
            return
        # second encounter of the dependency in this dependency tree
        if bpkgn in encountered:
            tidx = curpath.index(bpkgn)
            curpath.append(bpkgn)
            logger.get().warn(
                "cycle encountered: " + " => ".join(curpath[tidx:])
            )
            cycled[bpkgn] = True
            curpath = []
            raise RuntimeError()
        # already tested: pass
        if bpkgn in tested:
            return
        pkgr = _read_pkg(tmpln, ppkg)
        # probably broken, just skip from testing
        if not pkgr:
            tested[bpkgn] = True
            return False
        # when testing dependencies, skip stuff depending on its own subpkgs
        subpkgs = {}
        subpkgs[pkgr.pkgname] = True
        for sp in pkgr.subpkg_list:
            subpkgs[sp.pkgname] = True
        # mark tested as well as encountered
        tested[bpkgn] = True
        encountered[bpkgn] = True
        # save in the informational path
        curpath.append(bpkgn)
        # build a unique set of dependencies without repeated items
        hdeps, tdeps, rdeps = dependencies.setup_depends(pkgr)
        deplist = []
        for sver, pkgn in hdeps:
            deplist.append(pkgn)
        for sver, pkgn in tdeps:
            deplist.append(pkgn)
        # for runtime dependencies, we gotta skip subpackages of self
        for origin, dep in rdeps:
            spkgn, pkgv, pkgop = autil.split_pkg_name(dep)
            if not spkgn:
                pkg.error(f"invalid runtime dependency: {dep}")
            if not spkgn in subpkgs:
                # resolve base package
                for r in pkgr.source_repositories:
                    pkgp = paths.distdir() / r / spkgn
                    if (pkgp / "template.py").is_file():
                        spkgn = pkgp.resolve().name
                deplist.append(spkgn)
        # convert to set and back to list, that way we make it unique
        deplist = list(set(deplist))
        # check each dep
        for dep in deplist:
            # stuff depending on broken packages is itself broken
            if not _cycle_check(dep, pkgr):
                tested[dep] = True
                return False
            tested[dep] = True
        # clean up the path/encountered set for correct recursive behavior
        curpath.pop()
        del encountered[bpkgn]
        return True

    for tmpln in tmpls:
        if tmpln in tested:
            continue
        try:
            _cycle_check(tmpln, None)
            tested[tmpln] = True
        except RuntimeError:
            # encountered a cycle
            pass
        encountered = {}
        curpath = []

def do_update_check(tgt):
    from cbuild.core import update_check, template, chroot, logger

    if len(cmdline.command) < 2:
        raise errors.CbuildException(f"update-check needs a target package")

    verbose = False

    if len(cmdline.command) > 2:
        verbose = True

    pkgn = cmdline.command[1]
    tmpl = template.read_pkg(
        pkgn, chroot.host_cpu(), True,
        False, 1, False, False, None, target = "lint",
        allow_broken = True
    )

    update_check.update_check(tmpl, verbose)

def do_dump(tgt):
    from cbuild.core import chroot, template

    import json

    pkgn = cmdline.command[1] if len(cmdline.command) >= 2 else None

    tmpls = _collect_tmpls(pkgn)

    def _read_pkg(pkgn):
        try:
            return template.read_pkg(
                pkgn, opt_arch if opt_arch else chroot.host_cpu(), True,
                False, 1, False, False, None, target = "lint",
                allow_broken = True
            )
        except PackageError:
            return None

    dumps = []

    for tmpln in tmpls:
        pkgr = _read_pkg(tmpln)
        dumps.append(pkgr.dump())

    print(json.dumps(dumps, indent = 4))

def do_pkg(tgt, pkgn = None, force = None, check = None, stage = 3):
    from cbuild.core import build, chroot, template, paths

    if force is None:
        force = opt_force
    if check is None:
        check = opt_check
    if not pkgn:
        if len(cmdline.command) <= 1:
            raise errors.CbuildException(f"{tgt} needs a package name")
        elif len(cmdline.command) > 2:
            raise errors.CbuildException(f"{tgt} needs only one package")
        pkgn = cmdline.command[1]
    rp = template.read_pkg(
        pkgn, opt_arch if opt_arch else chroot.host_cpu(), force,
        check, opt_makejobs, opt_gen_dbg, opt_ccache, None,
        target = tgt if (tgt != "pkg") else None,
        force_check = opt_forcecheck, stage = stage
    )
    if opt_mdirtemp:
        chroot.install(chroot.host_cpu())
    # don't remove builddir/destdir
    paths.prepare()
    chroot.repo_sync()
    build.build(
        tgt, rp, {}, opt_signkey, dirty = opt_dirty,
        keep_temp = opt_keeptemp, check_fail = opt_checkfail
    )
    if tgt == "pkg" and (not opt_stage or stage < 3):
        do_unstage(tgt, stage < 3)

def _bulkpkg(pkgs, statusf):
    import pathlib
    import graphlib
    import traceback

    from cbuild.core import logger, template, paths, chroot, errors, build

    # we will use this for correct dependency ordering
    depg = graphlib.TopologicalSorter()
    visited = {}
    templates = {}
    failed = False
    log = logger.get()

    if opt_mdirtemp:
        chroot.install(chroot.host_cpu())
    paths.prepare()
    chroot.repo_sync()

    def _do_with_exc(f):
        # we are setting this
        nonlocal failed
        try:
            retv = f()
            if retv:
                return retv
        except template.SkipPackage:
            return False
        except errors.CbuildException as e:
            log.out_red(f"cbuild: {str(e)}")
            if e.extra:
                log.out_plain(e.extra)
            failed = True
            return False
        except errors.TracebackException as e:
            log.out_red(str(e))
            traceback.print_exc(file = log.estream)
            failed = True
            return False
        except errors.PackageException as e:
            e.pkg.log_red(f"ERROR: {e}", e.end)
            traceback.print_exc(file = log.estream)
            failed = True
            return False
        except Exception:
            logger.get().out_red("A failure has occurred!")
            traceback.print_exc(file = log.estream)
            failed = True
            return False
        # signal we're continuing
        return True

    # parse out all the templates first and grab their build deps
    for pn in pkgs:
        if pn in visited:
            continue
        # also mark visited under original name to skip further occurences
        visited[pn] = True
        # skip if previously failed and set that way
        if failed and opt_bulkfail:
            statusf.write(f"{pn} skipped\n")
            continue
        pp = pathlib.Path(pn)
        # resolve
        if pp.is_symlink():
            # resolve to the main package
            ln = pp.readlink()
            pp = pathlib.Path(f"{pl}/{ln}")
        # mark visited under a validated name just in case it differs
        visited[str(pp)] = True
        # validate
        pl = pp.parts
        if len(pl) != 2 or len(pl[0]) == 0 or \
           len(pl[1]) == 0 or pp.is_symlink():
            statusf.write(f"{pn} invalid\n")
            log.out_red(f"cbuild: invalid package '{pn}'")
            failed = True
            continue
        # check if it's points to final template
        if not pp.is_dir() or not (pp / "template.py").is_file():
            statusf.write(f"{pn} missing\n")
            log.out_red(f"cbuild: missing package '{pn}'")
            failed = True
            continue
        # parse, handle any exceptions so that we can march on
        ofailed = failed
        failed = False
        tp = _do_with_exc(lambda: template.read_pkg(
            str(pp), opt_arch if opt_arch else chroot.host_cpu(),
            opt_force, opt_check, opt_makejobs, opt_gen_dbg, opt_ccache,
            None, target = None, force_check = opt_forcecheck, stage = 3
        ))
        if not tp:
            if failed:
                statusf.write(f"{pn} parse\n")
            else:
                failed = ofailed
            continue
        failed = ofailed
        # record the template for later use
        templates[tp.pkgname] = tp
        # add it into t graph with all its build deps
        bdl = tp.get_build_deps()
        depg.add(tp.pkgname, *bdl)

    # try building in sorted order
    if not failed or not opt_bulkfail:
        for pn in depg.static_order():
            # skip things that were not in the initial set
            if not pn in templates:
                continue
            # if we previously failed and want it this way, skip the rest
            if failed and opt_bulkfail:
                statusf.write(f"{pn} skipped\n")
                continue
            # ensure to write the status
            if _do_with_exc(lambda: build.build(
                "pkg", templates[pn], {}, opt_signkey, dirty = False,
                keep_temp = False, check_fail = opt_checkfail
            )):
                statusf.write(f"{pn} ok\n")
            else:
                statusf.write(f"{pn} failed\n")

    if failed:
        raise errors.CbuildException(f"at least one bulk-pkg package failed")
    elif not opt_stage:
        do_unstage("pkg", False)

def do_bulkpkg(tgt):
    import os

    if len(cmdline.command) <= 1:
        raise errors.CbuildException(f"bulk-pkg needs at least one package")
    pkgs = cmdline.command[1:]

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
        _bulkpkg(pkgs, sout)
    except:
        sout.close()
        raise

#
# MAIN ENTRYPOINT
#

def fire():
    import os
    import sys
    import shutil
    import traceback
    import subprocess

    from cbuild.core import chroot, logger, template, profile
    from cbuild.core import scanelf, paths, errors
    from cbuild.apk import cli

    logger.init(not opt_nocolor)

    # check container and while at it perform arch checks
    chroot.chroot_check()

    # ensure we've got a signing key
    if not opt_signkey and not opt_unsigned and cmdline.command[0] != "keygen":
        logger.get().out_red("cbuild: no signing key set")
        sys.exit(1)

    # initialize profiles
    profile.init(global_cfg)

    # check target arch validity if provided
    if opt_arch:
        try:
            profile.get_profile(opt_arch)
        except:
            logger.get().out_red(
                f"cbuild: unknown target architecture '{opt_arch}'"
            )
            sys.exit(1)
    # let apk know if we're using network
    cli.set_network(not opt_nonet)

    try:
        aret = subprocess.run(
            [paths.apk(), "--version"], capture_output = True
        )
    except FileNotFoundError:
        logger.get().out_red(f"cbuild: apk not found ({paths.apk()}")
        sys.exit(1)

    if not aret.stdout.startswith(b"apk-tools 3"):
        logger.get().out_red("cbuild: apk-tools 3.x is required")
        sys.exit(1)

    apath = shutil.which(paths.apk())

    if scanelf.is_static(apath):
        logger.get().out_red("cbuild: static apk-tools is not supported")
        sys.exit(1)

    template.register_hooks()

    try:
        cmd = cmdline.command[0]
        match cmd:
            case "binary-bootstrap": binary_bootstrap(cmd)
            case "bootstrap": bootstrap(cmd)
            case "bootstrap-update": bootstrap_update(cmd)
            case "keygen": do_keygen(cmd)
            case "chroot": do_chroot(cmd)
            case "clean": do_clean(cmd)
            case "remove-autodeps": do_remove_autodeps(cmd)
            case "prune-obsolete": do_prune_obsolete(cmd)
            case "prune-removed": do_prune_removed(cmd)
            case "index": do_index(cmd)
            case "zap": do_zap(cmd)
            case "lint": do_lint(cmd)
            case "cycle-check": do_cycle_check(cmd)
            case "update-check": do_update_check(cmd)
            case "dump": do_dump(cmd)
            case "fetch" | "extract" | "prepare": do_pkg(cmd)
            case "patch" | "configure" | "build": do_pkg(cmd)
            case "check" | "install" | "pkg": do_pkg(cmd)
            case "unstage": do_unstage(cmd)
            case "bulk-pkg": do_bulkpkg(cmd)
            case _:
                logger.get().out_red(f"cbuild: invalid target {cmd}")
                sys.exit(1)
    except template.SkipPackage:
        pass
    except errors.CbuildException as e:
        logger.get().out_red(f"cbuild: {str(e)}")
        if e.extra:
            logger.get().out_plain(e.extra)
        sys.exit(1)
    except errors.TracebackException as e:
        logger.get().out_red(str(e))
        traceback.print_exc(file = logger.get().estream)
        sys.exit(1)
    except errors.PackageException as e:
        e.pkg.log_red(f"ERROR: {e}", e.end)
        traceback.print_exc(file = logger.get().estream)
        sys.exit(1)
    except:
        logger.get().out_red("A failure has occurred!")
        traceback.print_exc(file = logger.get().estream)
        sys.exit(1)
    finally:
        if opt_mdirtemp and not opt_keeptemp:
            shutil.rmtree(paths.bldroot())
