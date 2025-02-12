pkgname = "liborcus"
pkgver = "0.20.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://gitlab.com/orcus/orcus"
source = f"{url}/-/archive/{pkgver}/liborcus-{pkgver}.tar.gz"
sha256 = "6b5afd71a85ba402ca6932fdeef8cd6d70142a2d8cdb816556c39d546d86e05a"


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
