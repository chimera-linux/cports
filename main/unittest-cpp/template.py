pkgname = "unittest-cpp"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
makedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Lightweight unit testing framework for C++"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/unittest-cpp/unittest-cpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "74852198877dc2fdebdc4e5e9bd074018bf8ee03a13de139bfe41f4585b2f5b9"
hardening = ["cfi", "vis"]
# the tests are run as a post-build step for whatever reason, and disabling
# UTPP_INCLUDE_TESTS_IN_BUILD disables the building of tests altogether
options = ["!check", "!lintstatic"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("unittest-cpp-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/include", "usr/lib/cmake", "usr/lib/pkgconfig"]
