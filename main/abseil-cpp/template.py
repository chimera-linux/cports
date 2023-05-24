pkgname = "abseil-cpp"
pkgver = "20230125.2"
pkgrel = 1
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
sha256 = "9a2b5752d7bfade0bdeee2701de17c9480620f8b237e1964c1b9967c75374906"
# tests are not built, require gtest
options = ["!check"]


@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
