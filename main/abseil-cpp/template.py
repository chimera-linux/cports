pkgname = "abseil-cpp"
pkgver = "20230802.0"
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
sha256 = "59d2976af9d6ecf001a81a35749a6e551a335b949d34918cfade07737b9d93c5"
# tests are not built, require gtest
options = ["!check"]


@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
