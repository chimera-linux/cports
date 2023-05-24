from cbuild.core import chroot, paths
from fnmatch import fnmatch
import pathlib
import tempfile
import shutil

suffixes = {
    "*.tar.lzma": "txz",
    "*.tar.lz": "tlz",
    "*.tlz": "tlz",
    "*.tar.xz": "txz",
    "*.txz": "txz",
    "*.tar.bz2": "tbz",
    "*.tbz": "tbz",
    "*.tar.gz": "tgz",
    "*.tgz": "tgz",
    "*.gz": "gz",
    "*.xz": "xz",
    "*.bz2": "bz2",
    "*.tar": "tar",
    "*.zip": "zip",
    "*.rpm": "rpm",
    "*.patch": "txt",
    "*.diff": "txt",
    "*.txt": "txt",
    "*.sh": "txt",
    "*.7z": "7z",
    "*.crate": "crate",
}


def extract_tar(pkg, fname, dfile, edir, sfx):
    # for bootstrap, use python's native extractor
    if pkg.stage == 0:
        import tarfile

        with tarfile.open(dfile) as tf:
            tf.extractall(path=edir)
        return True

    return (
        chroot.enter(
            "tar",
            "-x",
            "--no-same-permissions",
            "--no-same-owner",
            "-f",
            dfile,
            "-C",
            edir,
            ro_root=True,
            unshare_all=True,
        ).returncode
        == 0
    )


def extract_notar(pkg, fname, dfile, edir, sfx):
    if sfx == "gz":
        cmd = "gunzip"
    elif sfx == "bz2":
        cmd = "bunzip2"
    elif sfx == "xz":
        cmd = "unxz"
    else:
        pkg.error(f"unknown suffix '{sfx}'")

    ofn = pathlib.Path(fname).stem
    opath = pkg.builddir / edir.name / ofn

    with open(opath, "wb") as outf:
        return (
            chroot.enter(
                cmd,
                "-c",
                "-f",
                dfile,
                ro_root=True,
                unshare_all=True,
                stdout=outf,
                wrkdir=edir,
            ).returncode
            == 0
        )


def extract_alsotar(pkg, fname, dfile, edir, sfx):
    return (
        chroot.enter(
            "tar", "-xf", dfile, "-C", edir, ro_root=True, unshare_all=True
        ).returncode
        == 0
    )


def extract_rpm(pkg, fname, dfile, edir, sfx):
    return (
        chroot.enter(
            "rpmextract", dfile, ro_root=True, unshare_all=True, wrkdir=edir
        ).returncode
        == 0
    )


def extract_txt(pkg, fname, dfile, edir, sfx):
    return (
        chroot.enter(
            "cp", "-f", dfile, edir, ro_root=True, unshare_all=True, wrkdir=edir
        ).returncode
        == 0
    )


def invoke(pkg):
    wpath = pkg.builddir / pkg.wrksrc
    # ensure that we start clean
    if wpath.exists():
        try:
            wpath.rmdir()
        except:
            pkg.error(f"cannot populate wrksrc (it exists and is dirty)")
    # now extract in a temporary place
    with tempfile.TemporaryDirectory(dir=pkg.builddir) as extractdir:
        # need to be able to manipulate it
        extractdir = pathlib.Path(extractdir)
        # go over each source and ensure extraction in the dir
        for d in pkg.source:
            doext = None
            # check if to skip extraction
            if isinstance(d, tuple):
                if len(d) > 2:
                    doext = d[2]
                elif isinstance(d[1], bool):
                    doext = d[1]
            # specifically False, skip
            if doext == False:
                continue
            # tuple-specified filename
            if isinstance(d, tuple) and not isinstance(d[1], bool):
                fname = d[1]
            else:
                fname = d[d.rfind("/") + 1 :]
            suffix = None
            for key in suffixes:
                if fnmatch(fname, key):
                    suffix = suffixes[key]
                    break
            if not suffix:
                pkg.error(f"unknown source suffix for '{fname}'")

            if pkg.stage == 0:
                if suffix != "tgz" and suffix != "tbz" and suffix != "txz":
                    pkg.error(f"source not supported for bootstrap: {fname}")

            match suffix:
                case "tar" | "txz" | "tbz" | "tlz" | "tgz" | "crate":
                    exf = extract_tar
                case "gz" | "bz2" | "xz":
                    exf = extract_notar
                case "zip" | "7z":
                    exf = extract_alsotar
                case "rpm":
                    exf = extract_rpm
                case "txt":
                    exf = extract_txt
                case _:
                    pkg.error(f"cannot guess '{fname}' extract suffix")

            if pkg.stage == 0:
                srcs_path = paths.sources()
            else:
                srcs_path = pathlib.Path("/sources")
            if not exf(
                pkg,
                fname,
                srcs_path / f"{pkg.pkgname}-{pkg.pkgver}/{fname}",
                pkg.chroot_builddir / extractdir.name,
                suffix,
            ):
                pkg.error(f"extracting '{fname}' failed (missing program?)")
        # try iterating it
        it = extractdir.iterdir()
        entry = None
        sentry = None
        try:
            # try to get two entries from the directory
            entry = next(it)
            sentry = next(it)
        except StopIteration:
            pass
        # no contents
        if not entry:
            return
        # in case wrksrc was declared to be multilevel
        wpath.parent.mkdir(parents=True, exist_ok=True)
        # if the extracted contents are a single real directory, use
        # it as wrksrc (rename appropriately); otherwise use a fresh
        # wrksrc and move all the extracted stuff in there
        if sentry or not entry.is_dir() or entry.is_symlink():
            # simply rename
            extractdir.rename(wpath)
        else:
            entry.rename(wpath)
    # all done; re-create the wrksrc in case nothing was extracted
    if not wpath.exists():
        wpath.mkdir(parents=True)
