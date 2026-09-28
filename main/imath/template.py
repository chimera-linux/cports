# bump all revdeps of openexr on major/minor (non-patch) bumps
pkgname = "imath"
pkgver = "3.2.3"
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
sha256 = "e10c12b3f21f45bf08e09d4215d9c7691368d747beebd840de0b6fefed2df9f8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("imath-devel")
def _(self):
    return self.default_devel()
