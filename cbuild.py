#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
import signal
import importlib
import traceback
import configparser

from os import path

from cbuild.core import paths

paths.init(path.dirname(__file__), "masterdir", "hostdir")

# start from a sane directory
os.chdir(path.dirname(__file__))

from cbuild.util import make
from cbuild.core import chroot, logger, template, build
from cbuild import cpu

from cbuild.apk import sign

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

args = parser.parse_args()

cmd = args.command

opt_gen_dbg = False

# read global configuration

global_cfg = configparser.ConfigParser()
global_cfg.read("etc/config.ini")

if "general" in global_cfg:
    gencfg = global_cfg["general"]
    make.set_jobs(gencfg.getint("jobs", fallback = 1))
    opt_gen_dbg = gencfg.getboolean("build_dbg", fallback = False)

signkey = None

if "signing" in global_cfg:
    signcfg = global_cfg["signing"]
    signkey = signcfg.get("key", fallback = None)

# set args options

if args.jobs:
    make.set_jobs(int(args.jobs))

if args.build_dbg:
    opt_gen_dbg = True

# ensure files are created with sane permissions
os.umask(0o022)

logger.init(not args.no_color and not "NO_COLOR" in os.environ)

# check masterdir and while at it perform arch checks
chroot.chroot_check()

# fix up environment
os.environ["CBUILD_ARCH"] = cpu.host()
os.environ["PATH"] = os.environ["PATH"] + ":" + \
    path.join(paths.masterdir(), "usr/bin")

# we should always be able to import modules from here
sys.path.append(path.dirname(__file__))

# create necessary directories
os.makedirs(paths.masterdir(), exist_ok = True)
os.makedirs(paths.hostdir(), exist_ok = True)
os.makedirs(paths.repository(), exist_ok = True)
os.makedirs(paths.sources(), exist_ok = True)

if not shutil.which("bwrap"):
    sys.exit("Required program not found: bwrap")

def do_exit(signum, stack):
    raise Exception("cbuild: interrupted!")

# exit handler
signal.signal(signal.SIGINT, do_exit)
signal.signal(signal.SIGTERM, do_exit)

def binary_bootstrap(tgt):
    if len(cmd) <= 1:
        chroot.install(cpu.host())
    else:
        chroot.install(cmd[1])

def bootstrap(tgt):
    rp = template.read_pkg("base-chroot", False, True, False, False, None)
    chroot.initdb()
    chroot.repo_sync()
    build.build(tgt, rp, {}, signkey)
    shutil.rmtree(paths.masterdir())
    chroot.install(cpu.host())

def bootstrap_update(tgt):
    chroot.update()

def do_keygen(tgt):
    if len(cmd) >= 3:
        keyn, keysize = cmd[1], int(cmd[2])
    elif len(cmd) >= 2:
        keyn, keysize = cmd[1], 2048
    else:
        keyn, keysize = None, 2048

    if not keyn or len(keyn) == 0:
        keyn = signkey

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
    pkgn = cmd[1] if len(cmd) >= 1 else None
    rp = template.read_pkg(
        pkgn, args.force, False, args.skip_if_exists, opt_gen_dbg, None
    )
    # don't remove builddir/destdir
    chroot.repo_sync()
    chroot.update(do_clean = False)
    chroot.remove_autodeps(False)
    build.build(tgt, rp, {}, signkey)

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
    }).get(cmd[0], do_bad)(cmd[0])
except template.SkipPackage:
    pass
except:
    logger.get().out_red("A failure has occured!")
    traceback.print_exc(file = logger.get().estream)
