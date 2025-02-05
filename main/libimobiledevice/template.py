pkgname = "libimobiledevice"
pkgver = "1.3.0"
pkgrel = 6
build_style = "gnu_configure"
configure_args = ["--disable-static"]  # prevent building python binding .a
hostmakedepends = [
    "pkgconf",
    "automake",
    "libtool",
    "python",
    "python-cython",
    "python-setuptools",
]
makedepends = [
    "python-devel",
    "glib-devel",
    "openssl3-devel",
    "libusb-devel",
    "libusbmuxd-devel",
    "libplist-devel",
]
pkgdesc = "Library to communicate with Apple devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libimobiledevice/archive/{pkgver}.tar.gz"
sha256 = "acbfb73eabee162e64c0d9de207d71c0a5f47c40cd5ad32a5097f734328ce10a"
options = ["!cross"]


@subpackage("libimobiledevice-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python3*"]


@subpackage("libimobiledevice-devel")
def _(self):
    return self.default_devel()


@subpackage("libimobiledevice-progs")
def _(self):
    return self.default_progs()
