def invoke(pkg):
    for v in pkg.destdir.rglob("*.py*"):
        if not v.is_file():
            continue
        if v.suffix != ".pyc" and v.suffix != ".pyo":
            continue
        v.unlink()
