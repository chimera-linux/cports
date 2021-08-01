from cbuild.core import chroot

import shutil
import pathlib
import subprocess

def process_patch(pkg, patchpath):
    pargs = "-Np1"
    argsf = pathlib.Path(str(patchpath) + ".args")

    if argsf.is_file():
        pargs = argsf.read_text().strip()
    elif pkg.patch_args:
        pargs = pkg.patch_args

    patchfn = patchpath.name
    patchsfx = patchpath.suffix

    try:
        shutil.copy(patchpath, pkg.builddir / pkg.wrksrc)
    except:
        pkg.error(f"could not copy patch '{patchfn}'")

    if patchsfx == ".gz":
        chroot.enter(
            "gunzip", [pkg.chroot_builddir / pkg.wrksrc / patchfn],
            check = True, bootstrapping = pkg.bootstrapping, ro_root = True
        )
        patchfn = patchpath.stem
    elif patchsfx == ".bz2":
        chroot.enter(
            "bunzip2", [pkg.chroot_builddir / pkg.wrksrc / patchfn],
            check = True, bootstrapping = pkg.bootstrapping, ro_root = True
        )
        patchfn = patchpath.stem
    elif patchsfx == ".diff" or patchsfx == ".patch":
        pass
    else:
        pkg.error(f"unknown patch type: {patchsfx}")

    pkg.log(f"patching: {patchfn}")

    chroot.enter(
        "patch", ["-sl", pargs, "-i", patchfn],
        stderr = subprocess.DEVNULL, check = True,
        wrkdir = pkg.chroot_builddir / pkg.wrksrc,
        bootstrapping = pkg.bootstrapping,
        ro_root = True
    )

def invoke(pkg):
    if not (pkg.builddir / pkg.wrksrc).is_dir():
        return
    if not pkg.patches_path.is_dir():
        return

    if (pkg.patches_path / "series").is_file():
        with open(pkg.patches_path / "series") as f:
            for line in f.readlines():
                process_patch(pkg, pkg.patches_path / line)
    else:
        for p in sorted(pkg.patches_path.glob("*")):
            if not p.is_file():
                continue
            if p.suffix == ".args":
                continue
            process_patch(pkg, p)
