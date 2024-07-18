pkgname = "benchmark"
pkgver = "1.8.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBENCHMARK_ENABLE_ASSEMBLY_TESTS=OFF",
    "-DBENCHMARK_ENABLE_DOXYGEN=OFF",
    "-DBENCHMARK_ENABLE_WERROR=OFF",
    "-DBENCHMARK_USE_BUNDLED_GTEST=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
checkdepends = ["gtest-devel"]
pkgdesc = "Microbenchmark support library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/benchmark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d26789a2b46d8808a48a4556ee58ccc7c497fcd4c0af9b90197674a81e04798a"


@subpackage("benchmark-devel")
def _devel(self):
    return self.default_devel()
