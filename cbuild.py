#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
import signal
import importlib
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
if not shutil.which("bwrap"):
    sys.exit("Required program not found: bwrap")

# global options

opt_gen_dbg   = False
opt_skipexist = False
opt_makejobs  = 1
opt_nocolor   = "NO_COLOR" in os.environ
opt_signkey   = None
opt_force     = False

# parse config file and set the global options from it

global_cfg = configparser.ConfigParser()
global_cfg.read("etc/config.ini")

if "general" in global_cfg:
    gencfg = global_cfg["general"]

    opt_gen_dbg  = gencfg.getboolean("build_dbg", fallback = False)
    opt_makejobs = gencfg.getint("jobs", fallback = 1)

if "signing" in global_cfg:
    signcfg = global_cfg["signing"]

    opt_signkey = signcfg.get("key", fallback = None)

# parse command line arguments

parser = argparse.ArgumentParser(description = "Chimera Linux build system.")

parser.add_argument(
    "-f", "--force", action = "store_const", const = True, default = False,
    help = "Force writing a package even when exists."
)
parser.add_argument(
    "-L", "--no-color", action = "store_const", const = True, default = False,
    help = "Force plain output."
)
parser.add_argument(
    "-j", "--jobs", help = "Number of jobs to use.", default = None
)
parser.add_argument(
    "-E", "--skip-if-exists", action = "store_const",
    const = True, default = False,
    help = "Do not build if the package already exists in local repository."
)
parser.add_argument(
    "-g", "--build-dbg", action = "store_const",
    const = True, default = False,
    help = "Build debug packages."
)
parser.add_argument("command", nargs = "+", help = "The command to issue.")

cmdline = parser.parse_args()

# command line args override config file

if cmdline.jobs:
    opt_makejobs = int(cmdline.jobs)

if cmdline.build_dbg:
    opt_gen_dbg = True

if cmdline.no_color:
    opt_nocolor = True

if cmdline.force:
    opt_force = True

if cmdline.skip_if_exists:
    opt_skipexist = True

# set global config bits as needed

from cbuild.core import paths

# init paths early, modules rely on it
paths.init(os.path.dirname(__file__), "masterdir", "hostdir")

from cbuild.util import make
from cbuild.core import chroot, logger, template, build
from cbuild.apk import sign
from cbuild import cpu

make.set_jobs(opt_makejobs)

logger.init(not opt_nocolor)

# check masterdir and while at it perform arch checks
chroot.chroot_check()

# fix up environment
os.environ["CBUILD_ARCH"] = cpu.host()
os.environ["PATH"] = os.environ["PATH"] + ":" + \
    str(paths.masterdir() / "usr/bin")

# create necessary directories
os.makedirs(paths.masterdir(), exist_ok = True)
os.makedirs(paths.hostdir(), exist_ok = True)
os.makedirs(paths.repository(), exist_ok = True)
os.makedirs(paths.sources(), exist_ok = True)

def binary_bootstrap(tgt):
    if len(cmdline.command) <= 1:
        chroot.install(cpu.host())
    else:
        chroot.install(cmdline.command[1])

def bootstrap(tgt):
    rp = template.read_pkg("base-chroot", False, True, False, False, None)
    chroot.initdb()
    chroot.repo_sync()
    build.build(tgt, rp, {}, opt_signkey)
    shutil.rmtree(paths.masterdir())
    chroot.install(cpu.host())

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

    sign.keygen(keyn, keysize)

def do_chroot(tgt):
    chroot.repo_sync()
    chroot.reconfigure()
    chroot.enter("/bin/cbuild-shell")

def do_clean(tgt):
    chroot.remove_autodeps(None)
    dirp = paths.masterdir() / "builddir"
    if dirp.is_dir():
        shutil.rmtree(dirp)
    elif dirp.exists():
        logger.get().out_red("cbuild: broken masterdir (builddir invalid)")
        return
    dirp = paths.masterdir() / "destdir"
    if dirp.is_dir():
        shutil.rmtree(dirp)
    elif dirp.exists():
        logger.get().out_red("cbuild: broken masterdir (destdir invalid)")
        return

def do_zap(tgt):
    if paths.masterdir().is_dir():
        shutil.rmtree(paths.masterdir())
    elif paths.masterdir().exists():
        logger.get().out_red("cbuild: broken masterdir")

def do_remove_autodeps(tgt):
    chroot.remove_autodeps(None)

def do_pkg(tgt):
    pkgn = cmdline.command[1] if len(cmdline.command) >= 1 else None
    rp = template.read_pkg(
        pkgn, opt_force, False, opt_skipexist, opt_gen_dbg, None
    )
    # don't remove builddir/destdir
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
