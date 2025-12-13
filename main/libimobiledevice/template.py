pkgname = "libimobiledevice"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]  # prevent building python binding .a
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "python",
    "python-cython",
    "python-setuptools",
]
makedepends = [
    "glib-devel",
    "libplist-devel",
    "libtatsu-devel",
    "libusb-devel",
    "libusbmuxd-devel",
    "openssl3-devel",
    "python-devel",
]
pkgdesc = "Library to communicate with Apple devices"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libimobiledevice/releases/download/{pkgver}/libimobiledevice-{pkgver}.tar.bz2"
sha256 = "23cc0077e221c7d991bd0eb02150a0d49199bcca1ddf059edccee9ffd914939d"
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
