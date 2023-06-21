def invoke(pkg):
    if not pkg._license_install or not pkg.options["distlicense"]:
        return

    has_license = False
    lpath = pkg.destdir / "usr/share/licenses"
    if lpath.is_dir():
        for f in lpath.iterdir():
            has_license = True
            break

    if not has_license:
        pkg.error("license installation necessary but no license installed")
