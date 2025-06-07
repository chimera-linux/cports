pkgname = "leveldb"
pkgver = "1.23"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_CXX_STANDARD=17",
    "-DLEVELDB_BUILD_BENCHMARKS=ON",
    "-DLEVELDB_BUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["benchmark-devel", "gtest-devel", "snappy-devel"]
pkgdesc = "Key/value database library"
license = "BSD-3-Clause"
url = "https://github.com/google/leveldb"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9a37f8a6174f09bd622bc723b55881dc541cd50747cbd08831c2a82d620f6d76"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("leveldb-devel")
def _(self):
    return self.default_devel()
