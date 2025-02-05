pkgname = "libplist"
pkgver = "2.6.0"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--disable-static"]  # prevent building python binding .a
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "python-cython",
    # distutils in configure
    "python-setuptools",
]
makedepends = ["python-devel", "glib-devel", "libxml2-devel"]
# transitional
provides = ["libplist++"]
pkgdesc = "Apple Property List library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libplist/releases/download/{pkgver}/libplist-{pkgver}.tar.bz2"
sha256 = "67be9ee3169366589c92dc7c22809b90f51911dd9de22520c39c9a64fb047c9c"
# FIXME int
hardening = ["!int"]
options = ["!cross"]


@subpackage("libplist-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python3*"]


@subpackage("libplist-devel")
def _(self):
    return self.default_devel()


@subpackage("libplist-progs")
def _(self):
    return self.default_progs()
