def invoke(pkg):
    if pkg.pkgname == "perl":
        return

    for f in pkg.destdir.rglob("*"):
        if not f.is_file():
            continue

        if f.name == "perllocal.pod":
            f.unlink()
        elif f.name == ".packlist":
            f.unlink()
