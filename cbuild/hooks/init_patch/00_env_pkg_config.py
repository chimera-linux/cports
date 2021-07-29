from cbuild.core import paths

def invoke(pkg):
    if not pkg.bootstrapping:
        return

    usrdir = paths.masterdir() / "usr"
    pkg.env["PKG_CONFIG_PATH"] = str(usrdir / "lib/pkgconfig") + ":" \
                               + str(usrdir / "share/pkgconfig")
