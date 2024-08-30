from cbuild.core import chroot, paths
from contextlib import contextmanager
from fnmatch import fnmatch
import pathlib
import tempfile

suffixes = {
    "*.tar.zst": "tzst",
    "*.tar.lzma": "txz",
    "*.tar.lz": "tlz",
    "*.tlz": "tlz",
    "*.tar.xz": "txz",
    "*.txz": "txz",
    "*.tar.bz2": "tbz",
    "*.tbz": "tbz",
    "*.tar.gz": "tgz",
    "*.tgz": "tgz",
    "*.zst": "zst",
    "*.gz": "gz",
    "*.xz": "xz",
    "*.bz2": "bz2",
    "*.tar": "tar",
    "*.zip": "zip",
    "*.rpm": "rpm",
    "*.deb": "deb",
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
    elif sfx == "zst":
        cmd = "unzstd"
    else:
        pkg.error(f"unknown source suffix '{sfx}'")

    ofn = pathlib.Path(fname).stem
    opath = pkg.statedir / edir.name / ofn

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


def extract_deb(pkg, fname, dfile, edir, sfx):
    with open(pkg.statedir / edir.name / "data", "wb") as outf:
        if (
            chroot.enter(
                "tar",
                "-xf",
                dfile,
                "-C",
                edir,
                "-O",
                "data.tar.*",
                ro_root=True,
                unshare_all=True,
                stdout=outf,
            ).returncode
            != 0
        ):
            return False

        # make sure stuff's committed to disk first before using from chroot
        outf.close()

        if (
            chroot.enter(
                "tar",
                "-xf",
                edir / "data",
                "-C",
                edir,
                ro_root=True,
                unshare_all=True,
            ).returncode
            != 0
        ):
            return False

    return True


def extract_txt(pkg, fname, dfile, edir, sfx):
    return (
        chroot.enter(
            "cp", "-f", dfile, edir, ro_root=True, unshare_all=True, wrkdir=edir
        ).returncode
        == 0
    )


def rename_edir(extractdir, wpath):
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
    wpath.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
    # if the extracted contents are a single real directory, use
    # it as the target (rename appropriately); otherwise use a fresh
    # target and move all the extracted stuff in there
    if sentry or not entry.is_dir() or entry.is_symlink():
        # simply rename
        extractdir.rename(wpath)
    else:
        entry.rename(wpath)


def invoke(pkg):
    wpath = pkg.srcdir
    # ensure that we start clean
    if wpath.exists():
        try:
            wpath.rmdir()
        except Exception:
            pkg.error("cannot populate wrksrc (it exists and is dirty)")
    edirs = None

    @contextmanager
    def close_edirs():
        try:
            yield
        finally:
            for sp, tmpd, tmpp in edirs:
                if not tmpd:
                    continue
                try:
                    rename_edir(tmpp, wpath / sp)
                finally:
                    tmpd.cleanup()

    # now extract in a temporary place
    with (
        tempfile.TemporaryDirectory(dir=pkg.statedir) as extractdir,
        close_edirs(),
    ):
        # need to be able to manipulate it
        extractdir = pathlib.Path(extractdir)
        if not pkg.source_paths:
            edirs = [("", None, extractdir)] * len(pkg.source)
        elif len(pkg.source_paths) != len(pkg.source):
            pkg.error("source_paths length must match sources")
        else:
            edirs = []
            for sp in pkg.source_paths:
                if not sp or sp == ".":
                    edirs.append(("", None, extractdir))
                    continue
                tdir = tempfile.TemporaryDirectory(dir=pkg.statedir)
                edirs.append((sp, tdir, pkg.statedir / tdir.name))
        # go over each source and ensure extraction in the dir
        for d, sp in zip(pkg.source, edirs):
            if d.startswith("!"):
                continue
            bkt = d.rfind(">")
            bsl = d.rfind("/")
            if bkt < 0 and bsl < 0:
                pkg.error(f"source '{d}' has an invalid format")
            if bkt > bsl:
                fname = d[bkt + 1 :]
            else:
                fname = d[bsl + 1 :]
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
                case "tar" | "txz" | "tbz" | "tlz" | "tzst" | "tgz" | "crate":
                    exf = extract_tar
                case "gz" | "bz2" | "xz":
                    exf = extract_notar
                case "zip" | "7z" | "rpm":
                    exf = extract_alsotar
                case "deb":
                    exf = extract_deb
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
                pkg.chroot_statedir / sp[2].name,
                suffix,
            ):
                pkg.error(
                    f"extracting '{fname}' failed",
                    hint="perhaps an extraction program is missing",
                )
        # handle the tempdir
        rename_edir(extractdir, wpath)
    # all done; re-create the wrksrc in case nothing was extracted
    if not wpath.exists():
        wpath.mkdir(parents=True)
