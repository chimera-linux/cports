pkgname = "unittest-cpp"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
make_check_target = "TestUnitTest++"
makedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Unit testing framework for C++"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/unittest-cpp/unittest-cpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "74852198877dc2fdebdc4e5e9bd074018bf8ee03a13de139bfe41f4585b2f5b9"
options = ["!lto"]


def post_install(self):
    self.install_license("LICENSE")
