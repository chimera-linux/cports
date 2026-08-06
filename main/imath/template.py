pkgname = "imath"
pkgver = "3.2.2"
pkgrel = 0
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
sha256 = "b4275d83fb95521510e389b8d13af10298ed5bed1c8e13efd961d91b1105e462"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("imath-devel")
def _(self):
    return self.default_devel()
