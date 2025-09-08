pkgname = "liborcus"
pkgver = "0.20.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool", "python"]
makedepends = [
    "boost-devel",
    "ixion-devel",
    "mdds",
    "python-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for processing spreadsheets"
license = "MPL-2.0"
url = "https://gitlab.com/orcus/orcus"
source = f"{url}/-/archive/{pkgver}/liborcus-{pkgver}.tar.gz"
sha256 = "bd7942cf43d3d62770be79a257c9d07a120c5b9cb0b3dc1799514cb83aa68f02"


@subpackage("liborcus-progs")
def _(self):
    return self.default_progs()


@subpackage("liborcus-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("liborcus-devel")
def _(self):
    return self.default_devel()
