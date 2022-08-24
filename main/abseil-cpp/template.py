pkgname = "abseil-cpp"
pkgver = "20220623.0"
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
sha256 = "4208129b49006089ba1d6710845a45e31c59b0ab6bff9e5788a87f55c5abd602"
# tests are not built, require gtest
options = ["!check"]

@subpackage("abseil-cpp-devel")
def _devel(self):
    return self.default_devel()
