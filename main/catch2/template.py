pkgname = "catch2"
pkgver = "3.7.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCATCH_BUILD_EXTRA_TESTS=ON",
    "-DCATCH_DEVELOPMENT_BUILD=ON",
    "-DCATCH_ENABLE_WERROR=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["python"]
pkgdesc = "C++-based test framework"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSL-1.0"
url = "https://github.com/catchorg/Catch2"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c991b247a1a0d7bb9c39aa35faf0fe9e19764213f28ffba3109388e62ee0269c"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("catch2-devel")
def _(self):
    return self.default_devel()
