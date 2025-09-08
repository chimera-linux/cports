pkgname = "ixion"
pkgver = "0.20.0"
pkgrel = 3
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = ["boost-devel", "python-devel", "mdds"]
checkdepends = ["bash"]
pkgdesc = "General-purpose formula parser and interpreter"
license = "MPL-2.0"
url = "https://gitlab.com/ixion/ixion"
source = f"{url}/-/archive/{pkgver}/ixion-{pkgver}.tar.gz"
sha256 = "4a6c2c480ad40b706ecf459dfca03f39351e12b48911c7c4803b75c823a1bcb1"


@subpackage("ixion-libs")
def _(self):
    return self.default_libs()


@subpackage("ixion-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("ixion-devel")
def _(self):
    return self.default_devel()
