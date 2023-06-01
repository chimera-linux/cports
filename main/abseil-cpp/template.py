pkgname = "abseil-cpp"
pkgver = "20230125.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_CXX_STANDARD=17",
    "-DBUILD_SHARED_LIBS=ON",
    "-DABSL_PROPAGATE_CXX_STD=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Abseil C++ libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://abseil.io"
source = (
    f"https://github.com/abseil/{pkgname}/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "5366d7e7fa7ba0d915014d387b66d0d002c03236448e1ba9ef98122c13b35c36"
# tests are not built, require gtest
options = ["!check"]


@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
