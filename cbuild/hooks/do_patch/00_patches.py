from cbuild.core import chroot

import os
import glob
import shutil
import subprocess

def process_patch(pkg, patchpath):
    pargs = "-Np0"
    argsf = patchpath + ".args"

    if os.path.isfile(argsf):
        with open(argsf) as f:
            pargs = f.read().strip()
    elif pkg.patch_args:
        pargs = pkg.patch_args

    _, patchfn = os.path.split(patchpath)
    _, patchsfx = os.path.splitext(patchfn)

    try:
        shutil.copy(patchpath, pkg.abs_wrksrc)
    except:
        pkg.error(f"could not copy patch '{patchfn}'")

    if patchsfx == ".gz":
        chroot.enter(
            "gunzip", [str(pkg.chroot_wrksrc / patchfn)], check = True
        )
        patchfn = os.path.splitext(patchfn)
    elif patchsfx == ".bz2":
        chroot.enter(
            "bunzip2", [str(pkg.chroot_wrksrc / patchfn)], check = True
        )
        patchfn = os.path.splitext(patchfn)
    elif patchsfx == ".diff" or patchsfx == ".patch":
        pass
    else:
        pkg.error(f"unknown patch type: {patchsfx}")

    pkg.log(f"patching: {patchfn}")

    chroot.enter("/usr/bin/cbuild-do", [
        pkg.chroot_wrksrc, "patch", "-sl", pargs, "-i", patchfn
    ], stderr = subprocess.DEVNULL, check = True)

def invoke(pkg):
    if not os.path.isdir(pkg.abs_wrksrc):
        return
    if not os.path.isdir(pkg.patches_path):
        return

    if os.path.isfile(pkg.patches_path / "series"):
        with open(pkg.patches_path / "series") as f:
            for line in f.readlines():
                process_patch(pkg, str(pkg.patches_path / line))
    else:
        for p in sorted(glob.glob(str(pkg.patches_path / "*"))):
            if not os.path.isfile(p):
                continue
            pr, pext = os.path.splitext(p)
            if pext == ".args":
                continue
            process_patch(pkg, p)
