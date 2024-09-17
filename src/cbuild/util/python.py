import pathlib


def precompile(pkg, path):
    path = pathlib.Path(path)

    if path.is_absolute():
        pkg.error(f"path '{path}' must not be absolute")

    apath = pkg.chroot_destdir / path

    pkg.do(
        "python3",
        "-m",
        "compileall",
        "-f",
        "-q",
        apath,
    )
