pkgname = "cereal"
pkgver = "1.3.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSKIP_PORTABILITY_TEST=ON",
    "-DSKIP_PERFORMANCE_COMPARISON=ON",
    "-DTHREAD_SAFE=ON",
    "-DWITH_WERROR=OFF",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["boost-devel"]
pkgdesc = "Header-only C++ serialization library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://uscilab.github.io/cereal"
source = f"https://github.com/USCiLab/cereal/archive/v{pkgver}.tar.gz"
sha256 = "16a7ad9b31ba5880dac55d62b5d6f243c3ebc8d46a3514149e56b5e7ea81f85f"


def post_install(self):
    self.install_license("LICENSE")
