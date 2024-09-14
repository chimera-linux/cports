pkgname = "benchmark"
pkgver = "1.9.0"
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
sha256 = "35a77f46cc782b16fac8d3b107fbfbb37dcd645f7c28eee19f3b8e0758b48994"


@subpackage("benchmark-devel")
def _(self):
    return self.default_devel()
