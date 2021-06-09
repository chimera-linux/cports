from cbuild.core import chroot
from fnmatch import fnmatch
import os

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

tar_cmd = None

def extract_tar(pkg, fname, dfile, edir, sfx):
    if chroot.enter(tar_cmd, [
        "-x", "--no-same-permissions", "--no-same-owner",
        "-f", str(dfile), "-C", edir
    ], bootstrapping = pkg.bootstrapping).returncode != 0:
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
        os.makedirs(pkg.abs_wrksrc, exist_ok = False)
        if not pkg.abs_wrksrc.is_dir():
            pkg.error(f"failed to create wrksrc")

    x = chroot.enter(
        "sh", ["-c", "command -v bsdtar"],
        capture_out = True, check = True,
        bootstrapping = pkg.bootstrapping
    )
    if len(x.stdout.strip()) == 0:
        x = chroot.enter(
            "sh", ["-c", "command -v tar"],
            capture_out = True, check = True,
            bootstrapping = pkg.bootstrapping
        )
    if len(x.stdout.strip()) == 0:
        pkg.error("no suitable tar command")

    global tar_cmd
    tar_cmd = x.stdout.strip().decode("ascii")

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

        if pkg.create_wrksrc:
            extractdir = pkg.chroot_wrksrc
        else:
            extractdir = pkg.chroot_builddir

        exf = extract_table.get(suffix, None)
        if not exf:
            pkg.error(f"cannot guess '{fname}' extract suffix")
        exf(pkg, fname, os.path.join(
            pkg.chroot_hostdir / "sources",
            f"{pkg.pkgname}-{pkg.version}", fname
        ), extractdir, suffix)
