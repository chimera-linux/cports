# nb: requires CXX14+ to use it
pkgname = "gtest"
pkgver = "1.13.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DCMAKE_SKIP_RPATH=ON"]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
pkgdesc = "Google's framework for writing C++ tests"
license = "BSD-3-Clause"
url = "https://github.com/google/googletest"
source = (
    f"https://github.com/google/googletest/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ad7fdba11ea011c1d925b3289cf4af2c66a352e18d4c7264392fead75e919363"
# no tests provided by upstream
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("gtest-devel")
def _devel(self):
    return self.default_devel()
