pkgname = "benchmark"
pkgver = "1.9.3"
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
license = "Apache-2.0"
url = "https://github.com/google/benchmark"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b94263b018042007eb53f79639f21ae47800808c73cf1b7df85622b6e2b1aa32"


@subpackage("benchmark-devel")
def _(self):
    return self.default_devel()
