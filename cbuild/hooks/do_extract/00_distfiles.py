from cbuild.core import chroot, paths
from fnmatch import fnmatch
import pathlib

suffixes = {
    "*.tar.lzma":   "txz",
    "*.tar.lz":     "tlz",
    "*.tlz":        "tlz",
    "*.tar.xz":     "txz",
    "*.txz":        "txz",
    "*.tar.bz2":    "tbz",
    "*.tbz":        "tbz",
    "*.tar.gz":     "tgz",
    "*.tgz":        "tgz",
    "*.gz":         "gz",
    "*.xz":         "xz",
    "*.bz2":        "bz2",
    "*.tar":        "tar",
    "*.zip":        "zip",
    "*.rpm":        "rpm",
    "*.patch":      "txt",
    "*.diff":       "txt",
    "*.txt":        "txt",
    "*.sh":         "txt",
    "*.7z":	        "7z",
    "*.gem":	    "gem",
    "*.crate":      "crate",
}

def extract_tar(pkg, fname, dfile, edir, sfx):
    # for bootstrap, use python's native extractor
    if pkg.bootstrapping:
        import tarfile
        with tarfile.open(dfile) as tf:
            tf.extractall(path = edir)
        return

    if chroot.enter("tar", [
        "-x", "--no-same-permissions", "--no-same-owner",
        "-f", dfile, "-C", edir
    ], ro_root = True).returncode != 0:
        pkg.error(f"extracting '{fname}' failed!")

def extract_notar(pkg, fname, dfile, edir, sfx):
    pass

def extract_zip(pkg, fname, dfile, edir, sfx):
    pass

def extract_rpm(pkg, fname, dfile, edir, sfx):
    pass

def extract_txt(pkg, fname, dfile, edir, sfx):
    pass

def extract_7z(pkg, fname, dfile, edir, sfx):
    pass

def extract_gem(pkg, fname, dfile, edir, sfx):
    pass

extract_table = {
    "tar": extract_tar,
    "txz": extract_tar,
    "tbz": extract_tar,
    "tlz": extract_tar,
    "tgz": extract_tar,
    "crate": extract_tar,

    "gz": extract_notar,
    "bz2": extract_notar,
    "xz": extract_notar,

    "zip": extract_zip,
    "rpm": extract_rpm,
    "txt": extract_txt,
    "7z": extract_7z,
    "gem": extract_gem,
}

def invoke(pkg):
    if pkg.create_wrksrc:
        (pkg.builddir / pkg.wrksrc).mkdir(exist_ok = True, parents = True)

    for d in pkg.distfiles:
        if isinstance(d, tuple):
            fname = d[1]
        else:
            fname = d[d.rfind("/") + 1:]
        if fname in pkg.skip_extraction:
            continue
        suffix = None
        for key in suffixes:
            if fnmatch(fname, key):
                suffix = suffixes[key]
                break
        if not suffix:
            pkg.error(f"unknown distfile suffix for '{fname}'")

        if pkg.bootstrapping:
            if suffix != "tgz" and suffix != "tbz" and suffix != "txz":
                pkg.error(f"distfile not supported for bootstrap: {fname}")

        if pkg.create_wrksrc:
            extractdir = pkg.builddir / pkg.wrksrc
        else:
            extractdir = pkg.chroot_builddir

        exf = extract_table.get(suffix, None)
        if not exf:
            pkg.error(f"cannot guess '{fname}' extract suffix")
        if pkg.bootstrapping:
            srcs_path = paths.hostdir() / "sources"
        else:
            srcs_path = pathlib.Path("/sources")
        exf(
            pkg, fname,
            srcs_path / f"{pkg.pkgname}-{pkg.version}/{fname}",
            extractdir, suffix
        )
