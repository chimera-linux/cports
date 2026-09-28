pkgname = "nlopt"
pkgver = "2.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library for nonlinear optimization"
license = "MIT"
url = "https://nlopt.readthedocs.io"
source = f"https://github.com/stevengj/nlopt/archive/v{pkgver}.tar.gz"
sha256 = "506f83a9e778ad4f204446e99509cb2bdf5539de8beccc260a014bd560237be1"


def post_install(self):
    self.install_license("COPYING")


@subpackage("nlopt-devel")
def _(self):
    return self.default_devel()
