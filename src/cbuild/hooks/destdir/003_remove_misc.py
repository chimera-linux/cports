def invoke(pkg):
    (pkg.destdir / "usr/lib/charset.alias").unlink(missing_ok=True)
    (pkg.destdir / "usr/share/info/dir").unlink(missing_ok=True)
