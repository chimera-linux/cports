pkgname = "liborcus"
pkgver = "0.21.0"
pkgrel = 0
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
sha256 = "2dc9bc0e4e22acf9752ff62d388c68fc66bd68138cbed8594982b147b415e186"


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
