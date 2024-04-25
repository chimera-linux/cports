pkgname = "imath"
pkgver = "3.1.11"
pkgrel = 1
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://imath.readthedocs.io/en/latest"
source = f"https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9057849585e49b8b85abe7cc1e76e22963b01bfdc3b6d83eac90c499cd760063"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("imath-devel")
def _devel(self):
    return self.default_devel()
