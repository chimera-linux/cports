def invoke(pkg):
    if pkg.options["keeplibtool"]:
        return

    for v in pkg.destdir.rglob("*.la"):
        v.unlink()
