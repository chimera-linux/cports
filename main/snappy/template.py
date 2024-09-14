pkgname = "snappy"
pkgver = "1.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DSNAPPY_BUILD_TESTS=OFF",
    "-DSNAPPY_BUILD_BENCHMARKS=OFF",
]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Fast compressor/decompressor"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://google.github.io/snappy"
source = f"https://github.com/google/snappy/archive/{pkgver}.tar.gz"
sha256 = "736aeb64d86566d2236ddffa2865ee5d7a82d26c9016b36218fcc27ea4f09f86"
# tests depend on in-tree gtest
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("snappy-devel")
def _(self):
    return self.default_devel()
