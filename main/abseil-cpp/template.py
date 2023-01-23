pkgname = "abseil-cpp"
pkgver = "20220623.1"
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
sha256 = "91ac87d30cc6d79f9ab974c51874a704de9c2647c40f6932597329a282217ba8"
# tests are not built, require gtest
options = ["!check"]

@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
