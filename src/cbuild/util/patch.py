from cbuild.core import chroot

import shutil
import pathlib
import subprocess

_gnupatch = None


def _determine_gnupatch(pkg):
    global _gnupatch

    # if a chroot is ready, it's never gnu patch
    if pkg.stage != 0:
        return False

    if _gnupatch is not None:
        return _gnupatch

    sr = subprocess.run(
        ["patch", "--version"], capture_output=True
    ).stdout.splitlines()

    _gnupatch = len(sr) > 0 and sr[0].startswith(b"GNU")
    return _gnupatch


def _patch_one(pkg, patch_path, wrksrc, patch_args):
    patch_path = pathlib.Path(patch_path)

    if not patch_path.is_file():
        pkg.error(f"patch does not exist: {patch_path}")

    pargs = ["-sNp1", *patch_args]

    # in bootstrap envs we might be using gnu patch with different args
    gnupatch = _determine_gnupatch(pkg)

    if not gnupatch:
        pargs += ["-z", ""]
    else:
        pargs.append("--no-backup-if-mismatch")

    patchfn = patch_path.name
    patchsfx = patch_path.suffix

    if patchsfx != ".patch":
        pkg.error(f"unknown patch type: {patchsfx}")

    wdir = pkg.srcdir
    cwdir = pkg.chroot_srcdir
    if wrksrc:
        wdir = wdir / wrksrc
        cwdir = cwdir / wrksrc

    try:
        shutil.copy(patch_path, wdir)
    except Exception:
        pkg.error(f"could not copy patch '{patchfn}'")

    pkg.log(f"patching: {patchfn}")

    chroot.enter(
        "patch",
        *pargs,
        "-i",
        cwdir / patchfn,
        stderr=subprocess.DEVNULL,
        check=True,
        wrkdir=cwdir,
        bootstrapping=pkg.stage == 0,
        ro_root=True,
    )


def patch(pkg, patch_list, wrksrc=None, patch_args=[]):
    for p in patch_list:
        _patch_one(pkg, p, wrksrc, patch_args)


def patch_git(pkg, patch_list, wrksrc=None, apply_args=[]):
    if len(patch_list) == 0:
        return

    # first init a git repository, apply won't work without it
    if subprocess.run(["git", "init", "-q"], cwd=pkg.srcdir).returncode != 0:
        pkg.error("failed to initialize repository in source location")

    # now apply everything in a batch
    srcmd = [
        "env",
        "HOME=/dev/null",
        "git",
        "apply",
        "--whitespace=nowarn",
        *apply_args,
    ]
    for p in patch_list:
        pkg.log(f"patching: {p.name}")
        if subprocess.run([*srcmd, p], cwd=pkg.srcdir).returncode != 0:
            pkg.error(f"failed to apply '{p.name}'")

    # now remove the repo so we don't give build systems ideas
    shutil.rmtree(pkg.srcdir / ".git")
