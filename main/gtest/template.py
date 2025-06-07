pkgname = "gtest"
pkgver = "1.17.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_SKIP_INSTALL_RPATH=ON",
    "-Dgmock_build_tests=ON",
    "-Dgtest_build_tests=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
pkgdesc = "Google's framework for writing C++ tests"
license = "BSD-3-Clause"
url = "https://github.com/google/googletest"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "65fab701d9829d38cb77c14acdc431d2108bfdbf8979e40eb8ae567edf10b27c"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("gtest-devel")
def _(self):
    return self.default_devel()
