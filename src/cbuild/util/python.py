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


def setup_wheel_venv(pkg, dest, target="dist/*.whl", args=[], wrapper=[]):
    whl = list(
        map(
            lambda p: str(p.relative_to(pkg.cwd)),
            pkg.cwd.glob(target),
        )
    )

    pkg.rm(dest, recursive=True, force=True)
    pkg.do(
        "python3",
        "-m",
        "venv",
        "--without-pip",
        "--system-site-packages",
        "--clear",
        dest,
    )

    pkg.do(
        *wrapper,
        pkg.chroot_cwd / dest / "bin/python3",
        "-m",
        "installer",
        "--compile-bytecode",
        "0",
        *args,
        *whl,
    )
