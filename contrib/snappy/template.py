pkgname = "snappy"
pkgver = "1.2.0"
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
sha256 = "9b8f10fbb5e3bc112f2e5e64f813cb73faea42ec9c533a5023b5ae08aedef42e"
# tests depend on in-tree gtest
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("snappy-devel")
def _devel(self):
    return self.default_devel()
