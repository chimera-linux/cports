from cbuild.core import chroot

import shutil
import pathlib
import subprocess

def process_patch(pkg, patchpath, gnupatch):
    pargs = ["-sNp1"]

    if not gnupatch:
        pargs += ["-z", ""]
    else:
        pargs.append("--no-backup-if-mismatch")

    argsf = pathlib.Path(str(patchpath) + ".args")

    if argsf.is_file():
        pargs += shlex.split(argsf.read_text().strip())
    elif pkg.patch_args:
        pargs += pkg.patch_args

    patchfn = patchpath.name
    patchsfx = patchpath.suffix

    try:
        shutil.copy(patchpath, pkg.builddir / pkg.wrksrc)
    except:
        pkg.error(f"could not copy patch '{patchfn}'")

    if patchsfx == ".gz":
        chroot.enter(
            "gunzip", [pkg.chroot_builddir / pkg.wrksrc / patchfn],
            check = True, bootstrapping = pkg.bootstrapping, ro_root = True,
            unshare_all = True
        )
        patchfn = patchpath.stem
    elif patchsfx == ".bz2":
        chroot.enter(
            "bunzip2", [pkg.chroot_builddir / pkg.wrksrc / patchfn],
            check = True, bootstrapping = pkg.bootstrapping, ro_root = True,
            unshare_all = True
        )
        patchfn = patchpath.stem
    elif patchsfx == ".diff" or patchsfx == ".patch":
        pass
    else:
        pkg.error(f"unknown patch type: {patchsfx}")

    pkg.log(f"patching: {patchfn}")

    chroot.enter(
        "patch", pargs + ["-i", pkg.chroot_cwd / patchfn],
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

    # in bootstrap envs we might be using gnu patch with different args
    gnupatch = False
    if pkg.bootstrapping:
        sr = subprocess.run(
            ["patch", "--version"], capture_output = True
        ).stdout.splitlines()
        gnupatch = len(sr) > 0 and sr[0].startswith(b"GNU")

    if (pkg.patches_path / "series").is_file():
        with open(pkg.patches_path / "series") as f:
            for line in f.readlines():
                process_patch(pkg, pkg.patches_path / line, gnupatch)
    else:
        for p in sorted(pkg.patches_path.glob("*")):
            if not p.is_file():
                continue
            if p.suffix == ".args":
                continue
            process_patch(pkg, p, gnupatch)
