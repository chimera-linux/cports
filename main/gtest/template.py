# nb: requires CXX14+ to use it
pkgname = "gtest"
pkgver = "1.15.0"
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
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "BSD-3-Clause"
url = "https://github.com/google/googletest"
source = (
    f"https://github.com/google/googletest/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "7315acb6bf10e99f332c8a43f00d5fbb1ee6ca48c52f6b936991b216c586aaad"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("gtest-devel")
def _devel(self):
    return self.default_devel()
