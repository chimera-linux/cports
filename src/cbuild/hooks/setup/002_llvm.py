from cbuild.core import paths


def invoke(pkg):
    if pkg.stage <= 0:
        return
    # determine highest llvm version
    pkg.llvm_version = -1
    for f in (paths.bldroot() / "usr/lib").glob("llvm*"):
        lver = f.name.removeprefix("llvm")
        # skip non-viable false positives
        if not (f / f"lib/libLLVM.so.{lver}.1").is_file():
            continue
        pkg.llvm_version = max(pkg.llvm_version, int(lver))
