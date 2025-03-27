pkgname = "benchmark"
pkgver = "1.9.2"
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
sha256 = "409075176168dc46bbb81b74c1b4b6900385b5d16bfc181d678afb060d928bd3"


@subpackage("benchmark-devel")
def _(self):
    return self.default_devel()
