def invoke(pkg):
    for v in pkg.destdir.rglob("*.la"):
        v.unlink()
