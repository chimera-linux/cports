from cbuild.core import paths

from os.path import join

def invoke(pkg):
    if not pkg.bootstrapping:
        return

    usrdir = join(paths.masterdir(), "usr")
    pkg.CFLAGS += ["-isystem", join(usrdir, "include")]
    pkg.LDFLAGS += [
        "-L" + join(usrdir, "lib"), "-Wl,-rpath-link=" + join(usrdir, "lib")
    ]
