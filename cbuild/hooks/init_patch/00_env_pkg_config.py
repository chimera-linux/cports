from cbuild.core import paths

from os.path import join

def invoke(pkg):
    if not pkg.bootstrapping:
        return

    usrdir = join(paths.masterdir(), "usr")
    pkg.env["PKG_CONFIG_PATH"] = join(usrdir, "lib/pkgconfig") + ":" \
                               + join(usrdir, "share/pkgconfig")
