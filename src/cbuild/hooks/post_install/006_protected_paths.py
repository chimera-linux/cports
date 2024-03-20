# if the package protects some paths, here we write the right files

import pathlib

_valid_pfx = {
    "-": True,
    "+": True,
    "@": True,
    "!": True,
}


def invoke(pkg):
    if len(pkg.protected_paths) == 0:
        return

    ppath = pkg.destdir / "etc/apk/protected_paths.d"
    ppath.mkdir(exist_ok=True, parents=True, mode=0o755)

    with open(ppath / f"apk-{pkg.pkgname}.list", "w") as outf:
        for pp in pkg.protected_paths:
            if pp[0:1] not in _valid_pfx:
                pkg.error(f"protected path '{pp}' has an invalid prefix")
            if pathlib.Path(pp[1:]).is_absolute():
                pkg.error(f"protected path '{pp}' is not relative")
            outf.write(f"{pp}\n")
