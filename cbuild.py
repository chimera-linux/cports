#!/usr/bin/env python3

import os
import sys
import shutil
import shlex
import argparse
import signal
import pathlib
import importlib
import tempfile
import traceback
import configparser

# start from a sane directory
os.chdir(os.path.dirname(__file__))

# ensure files are created with sane permissions
os.umask(0o022)

# we should always be able to import modules from here
sys.path.append(os.path.dirname(__file__))

def do_exit(signum, stack):
    raise Exception("cbuild: interrupted!")

# exit handler
signal.signal(signal.SIGINT, do_exit)
signal.signal(signal.SIGTERM, do_exit)

# program checks
for prog in [
    "bwrap", "scanelf", "openssl", "apk", "git", "tee"
]:
    if not shutil.which(prog):
        sys.exit(f"Required program not found: {prog}")

# global options

opt_cflags    = "-O2"
opt_cxxflags  = "-O2"
opt_ldflags   = ""
opt_arch      = None
opt_gen_dbg   = False
opt_skipexist = False
opt_check     = True
opt_ccache    = False
opt_makejobs  = 1
opt_nocolor   = "NO_COLOR" in os.environ
opt_signkey   = None
opt_unsigned  = False
opt_allowroot = False
opt_force     = False
opt_mdirtemp  = False
opt_masterdir = "masterdir"
opt_hostdir   = "hostdir"

# parse command line arguments

parser = argparse.ArgumentParser(description = "Chimera Linux build system.")

parser.add_argument(
    "-c", "--config", default = "etc/config.ini",
    help = "The configuration file to use."
)
parser.add_argument(
    "-f", "--force", action = "store_const", const = True, default = opt_force,
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
    "-E", "--skip-if-exists", action = "store_const",
    const = True, default = opt_skipexist,
    help = "Do not build if the package already exists in local repository."
)
parser.add_argument(
    "-C", "--skip-check", action = "store_const",
    const = False, default = opt_check,
    help = "Skip running the check stage."
)
parser.add_argument(
    "-g", "--build-dbg", action = "store_const",
    const = True, default = opt_gen_dbg,
    help = "Build debug packages."
)
parser.add_argument(
    "-a", "--arch", help = "Target architecture to build for.", default = None
)
parser.add_argument(
    "-m", "--masterdir", default = None, help = "The masterdir path."
)
parser.add_argument(
    "-H", "--hostdir", default = None, help = "The hostdir path."
)
parser.add_argument(
    "-t", "--temporary", action = "store_const",
    const = True, default = opt_mdirtemp,
    help = "Use a temporary masterdir to build."
)
parser.add_argument(
    "--allow-unsigned", action = "store_const",
    const = True, default = opt_unsigned,
    help = "Allow building without a signing key."
)
parser.add_argument(
    "--allow-root", action = "store_const",
    const = True, default = opt_allowroot,
    help = "Allow running as root."
)
parser.add_argument("command", nargs = "+", help = "The command to issue.")

cmdline = parser.parse_args()

# parse config file and set the global options from it

global_cfg = configparser.ConfigParser()
global_cfg.read(cmdline.config)

if "build" in global_cfg:
    bcfg = global_cfg["build"]

    opt_gen_dbg   = bcfg.getboolean("build_dbg", fallback = opt_gen_dbg)
    opt_ccache    = bcfg.getboolean("ccache", fallback = opt_ccache)
    opt_check     = bcfg.getboolean("check", fallback = opt_check)
    opt_makejobs  = bcfg.getint("jobs", fallback = opt_makejobs)
    opt_cflags    = bcfg.get("cflags", fallback = opt_cflags)
    opt_cxxflags  = bcfg.get("cxxflags", fallback = opt_cxxflags)
    opt_ldflags   = bcfg.get("ldflags", fallback = opt_ldflags)
    opt_arch      = bcfg.get("arch", fallback = opt_arch)
    opt_masterdir = bcfg.get("masterdir", fallback = opt_masterdir)
    opt_hostdir   = bcfg.get("hostdir", fallback = opt_hostdir)

if "signing" in global_cfg:
    signcfg = global_cfg["signing"]

    opt_signkey = signcfg.get("key", fallback = opt_signkey)

# command line args override config file

if cmdline.jobs:
    opt_makejobs = int(cmdline.jobs)

if cmdline.build_dbg:
    opt_gen_dbg = True

if cmdline.arch:
    opt_arch = cmdline.arch

if cmdline.no_color:
    opt_nocolor = True

if cmdline.force:
    opt_force = True

if cmdline.skip_if_exists:
    opt_skipexist = True

if cmdline.skip_check:
    opt_check = False

if cmdline.masterdir:
    opt_masterdir = cmdline.masterdir

if cmdline.hostdir:
    opt_hostdir = cmdline.hostdir

if cmdline.temporary:
    mdp = pathlib.Path.cwd() / opt_masterdir
    # the temporary directory should be in the same location as masterdir
    opt_mdirtemp  = True
    opt_masterdir = tempfile.mkdtemp(
        prefix = mdp.name + ".", dir = mdp.parent
    )

# set global config bits as needed

from cbuild.core import paths

# init paths early, modules rely on it
paths.init(os.path.dirname(__file__), opt_masterdir, opt_hostdir)

from cbuild.util import make
from cbuild.core import chroot, logger, template, build, profile
from cbuild.apk import sign, cli as apk_cli

logger.init(not opt_nocolor)

# check masterdir and while at it perform arch checks
chroot.chroot_check()

# ensure we don't run as root
if not opt_allowroot and os.geteuid() == 0:
    logger.get().out_red("cbuild: please don't run as root")
    sys.exit(1)

# ensure we've got a signing key
if not opt_signkey and not opt_unsigned and cmdline.command[0] != "keygen":
    logger.get().out_red("cbuild: no signing key set")
    sys.exit(1)

# fix up environment
os.environ["CBUILD_ARCH"] = chroot.host_cpu()
os.environ["PATH"] = os.environ["PATH"] + ":" + \
    str(paths.masterdir() / "usr/bin")

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

def binary_bootstrap(tgt):
    paths.prepare()

    if len(cmdline.command) <= 1:
        chroot.install(chroot.host_cpu())
    else:
        chroot.install(cmdline.command[1])

def bootstrap(tgt):
    max_stage = 2

    if len(cmdline.command) > 1:
        max_stage = int(cmdline.command[1])

    oldmdir = paths.masterdir()

    paths.set_stage(0)
    paths.reinit_masterdir(oldmdir, 0)

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

        rp = template.read_pkg(
            "main/base-chroot", None, False, False, False, opt_makejobs,
            False, False, None
        )
        paths.prepare()
        chroot.initdb()
        chroot.repo_sync()
        build.build(tgt, rp, {}, opt_signkey)
        shutil.rmtree(paths.masterdir())
        chroot.install(chroot.host_cpu())

    if max_stage == 0:
        return

    # change binary repo path
    paths.set_stage(1)
    # set masterdir to stage 1 for chroot check
    paths.reinit_masterdir(oldmdir, 1)

    if not chroot.chroot_check(True):
        logger.get().out("cbuild: bootstrapping stage 1")
        # use stage 0 masterdir to build, but build into stage 1 repo
        paths.reinit_masterdir(oldmdir, 0)
        do_pkg("pkg", "main/base-chroot")
        # go back to stage 1
        paths.reinit_masterdir(oldmdir, 1)
        chroot.install(chroot.host_cpu())

    if max_stage == 1:
        return

    # change binary repo path
    paths.set_stage(2)
    # set masterdir to stage 2 for chroot check
    paths.reinit_masterdir(oldmdir, 2)

    if not chroot.chroot_check(True):
        logger.get().out("cbuild: bootstrapping stage 2")
        # use stage 1 masterdir to build, but build into stage 2 repo
        paths.reinit_masterdir(oldmdir, 1)
        do_pkg("pkg", "main/base-chroot")
        # go back to stage 2
        paths.reinit_masterdir(oldmdir, 2)
        chroot.install(chroot.host_cpu())

def bootstrap_update(tgt):
    chroot.update()

def do_keygen(tgt):
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
    if opt_mdirtemp:
        chroot.install(chroot.host_cpu())
    paths.prepare()
    chroot.repo_sync(True)
    chroot.reconfigure()
    chroot.enter(
        "/bin/cbuild-shell", pretend_uid = 0, pretend_gid = 0,
        mount_binpkgs = True, mount_ccache = True
    )

def do_clean(tgt):
    chroot.remove_autodeps(None)
    dirp = paths.masterdir() / "builddir"
    if dirp.is_dir():
        shutil.rmtree(dirp)
    elif dirp.exists():
        logger.get().out_red("cbuild: broken masterdir (builddir invalid)")
        raise Exception()
    dirp = paths.masterdir() / "destdir"
    if dirp.is_dir():
        shutil.rmtree(dirp)
    elif dirp.exists():
        logger.get().out_red("cbuild: broken masterdir (destdir invalid)")
        raise Exception()

def do_zap(tgt):
    if paths.masterdir().is_dir():
        shutil.rmtree(paths.masterdir())
    elif paths.masterdir().exists():
        logger.get().out_red("cbuild: broken masterdir")
        raise Exception()

def do_remove_autodeps(tgt):
    chroot.remove_autodeps(None)

def do_prune_obsolete(tgt):
    logger.get().out("cbuild: pruning repositories...")
    # ensure we know what cpu arch we are dealing with
    chroot.chroot_check()

    with open(paths.hostdir() / "repositories") as repof:
        for ln in repof:
            ln = ln.strip()
            if ln.startswith("#"):
                continue
            apk_cli.prune(pathlib.Path(ln))

def do_pkg(tgt, pkgn = None):
    if not pkgn:
        pkgn = cmdline.command[1] if len(cmdline.command) >= 1 else None
    rp = template.read_pkg(
        pkgn, opt_arch if opt_arch else chroot.host_cpu(), opt_force,
        opt_skipexist, opt_check, opt_makejobs, opt_gen_dbg, opt_ccache, None
    )
    if opt_mdirtemp:
        chroot.install(chroot.host_cpu())
    # don't remove builddir/destdir
    paths.prepare()
    chroot.repo_sync()
    chroot.update(do_clean = False)
    chroot.remove_autodeps(False)
    build.build(tgt, rp, {}, opt_signkey)

def do_bad(tgt):
    logger.get().out_red("cbuild: invalid target " + tgt)
    sys.exit(1)

template.register_hooks()

try:
    ({
        "binary-bootstrap": binary_bootstrap,
        "bootstrap": bootstrap,
        "bootstrap-update": bootstrap_update,
        "keygen": do_keygen,
        "chroot": do_chroot,
        "clean": do_clean,
        "remove-autodeps": do_remove_autodeps,
        "prune-obsolete": do_prune_obsolete,
        "zap": do_zap,
        "fetch": do_pkg,
        "extract": do_pkg,
        "patch": do_pkg,
        "configure": do_pkg,
        "build": do_pkg,
        "check": do_pkg,
        "install": do_pkg,
        "pkg": do_pkg
    }).get(cmdline.command[0], do_bad)(cmdline.command[0])
except template.SkipPackage:
    pass
except:
    logger.get().out_red("A failure has occured!")
    traceback.print_exc(file = logger.get().estream)
    sys.exit(1)
finally:
    if opt_mdirtemp:
        shutil.rmtree(paths.masterdir())
