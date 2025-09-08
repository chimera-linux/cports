pkgname = "imath"
pkgver = "3.1.12"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DPYTHON=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
]
pkgdesc = "C++ library of 2D and 3D vector, matrix, and math operations"
license = "BSD-3-Clause"
url = "https://imath.readthedocs.io/en/latest"
source = f"https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8a1bc258f3149b5729c2f4f8ffd337c0e57f09096e4ba9784329f40c4a9035da"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("imath-devel")
def _(self):
    return self.default_devel()
