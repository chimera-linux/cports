pkgname = "abseil-cpp"
pkgver = "20230125.1"
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
sha256 = "81311c17599b3712069ded20cca09a62ab0bf2a89dfa16993786c8782b7ed145"
# tests are not built, require gtest
options = ["!check"]

@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
