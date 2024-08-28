import bz2
import gzip


def invoke(pkg):
    for f in (pkg.destdir / "usr/share/man").rglob("*.*"):
        # sanitize
        if not f.is_file():
            continue
        # skip irrelevant files
        if f.suffix != ".gz" and f.suffix != ".bz2":
            continue
        # rewrite symlinks
        if f.is_symlink():
            f.with_suffix("").symlink_to(f.readlink().with_suffix(""))
            continue
        # uncompress
        gf = gzip.open(f, "rb") if f.suffix == ".gz" else bz2.open(f, "rb")
        with open(f.with_suffix(""), "wb") as uf:
            uf.write(gf.read())
        gf.close()
        f.unlink()
