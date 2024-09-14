pkgname = "eigen"
pkgver = "3.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "C++ template library for linear algebra"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "MPL-2.0 AND BSD-3-Clause AND Minpack AND Apache-2.0"
url = "https://gitlab.com/libeigen/eigen"
source = f"{url}/-/archive/{pkgver}/eigen-{pkgver}.tar.bz2"
sha256 = "b4c198460eba6f28d34894e3a5710998818515104d6e74e5cc331ce31e46e626"
# tests require autodiff
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.BSD")
