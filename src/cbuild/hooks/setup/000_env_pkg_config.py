from cbuild.core import paths


def invoke(pkg):
    if pkg.stage > 0:
        return

    usrdir = paths.bldroot() / "usr"
    pkg.env["PKG_CONFIG_PATH"] = (
        str(usrdir / "lib/pkgconfig") + ":" + str(usrdir / "share/pkgconfig")
    )
