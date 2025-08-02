from cbuild.core import chroot, paths

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


def patch(pkg, patch_list, wrksrc=None, patch_args=[], stamp=False):
    for p in patch_list:
        if stamp:
            with pkg.stamp(f"patch_{p.name}") as s:
                s.check()
                _patch_one(pkg, p, wrksrc, patch_args)
        else:
            _patch_one(pkg, p, wrksrc, patch_args)


def patch_git(pkg, patch_list, wrksrc=None, apply_args=[], stamp=False):
    if len(patch_list) == 0:
        return

    # first init a git repository, apply won't work without it
    if subprocess.run(["git", "init", "-q"], cwd=pkg.srcdir).returncode != 0:
        pkg.error("failed to initialize repository in source location")

    if (
        subprocess.run(
            ["git", "config", "--local", "gc.auto", "0"], cwd=pkg.srcdir
        ).returncode
        != 0
    ):
        pkg.error("failed setting initial git repository config")

    # now apply everything in a batch
    srcmd = [
        "env",
        "HOME=/dev/null",
        "git",
        "apply",
        "--whitespace=nowarn",
        *apply_args,
    ]

    def _apply(p):
        if subprocess.run([*srcmd, p], cwd=pkg.srcdir).returncode != 0:
            pkg.log(f"failed to apply '{p.name}', repeating in verbose mode")
            subprocess.run([*srcmd, "--verbose", p], cwd=pkg.srcdir)
            pkg.error(f"failed to apply '{p.name}'")

    relative_srcdir_path = pkg.srcdir.resolve().relative_to(paths.distdir())

    for p in patch_list:
        pkg.log(f"patching {relative_srcdir_path}: {p.name}")
        if stamp:
            with pkg.stamp(f"patch_{p.name}") as s:
                s.check()
                _apply(p)
        else:
            _apply(p)

    # now remove the repo so we don't give build systems ideas
    shutil.rmtree(pkg.srcdir / ".git")
