pkgname = "benchmark"
pkgver = "1.9.4"
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
makedepends = ["gtest-devel"]
pkgdesc = "Microbenchmark support library"
license = "Apache-2.0"
url = "https://github.com/google/benchmark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b334658edd35efcf06a99d9be21e4e93e092bd5f95074c1673d5c8705d95c104"


@subpackage("benchmark-devel")
def _(self):
    return self.default_devel()
