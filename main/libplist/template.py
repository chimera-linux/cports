pkgname = "libplist"
pkgver = "2.7.0"
pkgrel = 0
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
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libplist/releases/download/{pkgver}/libplist-{pkgver}.tar.bz2"
sha256 = "7ac42301e896b1ebe3c654634780c82baa7cb70df8554e683ff89f7c2643eb8b"
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
