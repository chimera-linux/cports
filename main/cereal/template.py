pkgname = "cereal"
pkgver = "1.3.2"
pkgrel = 1
build_style = "cmake"
# -m32 unsupported + broken in fortify-headers
configure_args = [
    "-DSKIP_PORTABILITY_TEST=ON",
    "-DBUILD_DOC=OFF",
    "-DBUILD_SANDBOX=OFF",
    "-DSKIP_PERFORMANCE_COMPARISON=ON",
    "-DWITH_WERROR=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
pkgdesc = "C++ library for serialization"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/USCiLab/cereal"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "16a7ad9b31ba5880dac55d62b5d6f243c3ebc8d46a3514149e56b5e7ea81f85f"


def post_install(self):
    self.install_license("LICENSE")
