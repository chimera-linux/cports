pkgname = "ixion"
pkgver = "0.19.0"
pkgrel = 5
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "python",
    "slibtool",
]
makedepends = ["boost-devel", "python-devel", "mdds"]
checkdepends = ["bash"]
pkgdesc = "General-purpose formula parser and interpreter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://gitlab.com/ixion/ixion"
source = f"{url}/-/archive/{pkgver}/ixion-{pkgver}.tar.gz"
sha256 = "b5b67ea7fc631a0fda4fff3123f0cc2e3831849bdd8fbae8443be0766a77f243"


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
