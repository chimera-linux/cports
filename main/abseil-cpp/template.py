pkgname = "abseil-cpp"
pkgver = "20211102.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DABSL_PROPAGATE_CXX_STD=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Abseil C++ libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://abseil.io"
source = f"https://github.com/abseil/{pkgname}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dcf71b9cba8dc0ca9940c4b316a0c796be8fab42b070bb6b7cab62b48f0e66c4"
# tests are not built, require gtest
options = ["!check"]

@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
