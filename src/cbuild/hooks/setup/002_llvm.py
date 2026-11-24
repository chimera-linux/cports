from cbuild.core import paths


def invoke(pkg):
    if pkg.stage <= 0:
        return
    # determine highest llvm version
    pkg.llvm_version = -1
    usr = paths.bldroot() / "usr"
    for f in (usr / "lib").glob("llvm*"):
        lver = f.name.removeprefix("llvm")
        # skip non-viable false positives
        if not (f / f"lib/libLLVM.so.{lver}.1").is_file():
            continue
        pkg.llvm_version = max(pkg.llvm_version, int(lver))
        # see if we have missing symlinks from wiped base-cbuild stuff
        if not (f / "bin/ld.lld").exists():
            (f / "bin/ld.lld").symlink_to("lld")
        if not (f / "bin/ld64.lld").exists():
            (f / "bin/ld64.lld").symlink_to("lld")
    # see if there are symlinks to restore in the main one
    pver = pkg.llvm_version
    # ld.lld
    if not (usr / "bin/ld.lld").exists():
        if (usr / f"bin/ld.lld-{pver}").exists():
            (usr / "bin/ld.lld").symlink_to(f"ld.lld-{pver}")
        else:
            (usr / "bin/ld.lld").symlink_to("lld")
    # ld64.lld
    if not (usr / "bin/ld64.lld").exists():
        if (usr / f"bin/ld64.lld-{pver}").exists():
            (usr / "bin/ld64.lld").symlink_to(f"ld64.lld-{pver}")
        else:
            (usr / "bin/ld64.lld").symlink_to("lld")
