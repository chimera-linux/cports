pkgname = "libplist"
pkgver = "2.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]  # prevent building python binding .a
hostmakedepends = ["pkgconf", "automake", "libtool", "python", "python-cython"]
makedepends = ["python-devel", "glib-devel", "libxml2-devel"]
pkgdesc = "Apple Property List library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = (
    f"https://github.com/libimobiledevice/{pkgname}/archive/{pkgver}.tar.gz"
)
sha256 = "7e654bdd5d8b96f03240227ed09057377f06ebad08e1c37d0cfa2abe6ba0cee2"
# FIXME int
hardening = ["!int"]
options = ["!cross"]


@subpackage("libplist++")
def _pp(self):
    self.pkgdesc = f"{pkgdesc} (C++ runtime library)"

    return ["usr/lib/libplist++*.so.*"]


@subpackage("libplist-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python3*"]


@subpackage("libplist-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libplist-progs")
def _progs(self):
    return self.default_progs()
