pkgname = "imath"
pkgver = "3.2.0"
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
sha256 = "f3c0c4210b5e6fe17d90cd7ebbe9638eea9fb458421d00eddb4d1a9d5ad47b36"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("imath-devel")
def _(self):
    return self.default_devel()
