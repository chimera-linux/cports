# nb: requires CXX14+ to use it
pkgname = "gtest"
pkgver = "1.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DCMAKE_SKIP_RPATH=ON"]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
pkgdesc = "Google's framework for writing C++ tests"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/google/googletest"
source = (
    f"https://github.com/google/googletest/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7"
# no tests provided by upstream
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("gtest-devel")
def _devel(self):
    return self.default_devel()
