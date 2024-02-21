pkgname = "catch2"
pkgver = "3.5.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCATCH_BUILD_EXTRA_TESTS=ON",
    "-DCATCH_DEVELOPMENT_BUILD=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["python"]
pkgdesc = "C++-based test framework"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "BSL-1.0"
url = "https://github.com/catchorg/Catch2"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "269543a49eb76f40b3f93ff231d4c24c27a7e16c90e47d2e45bcc564de470c6e"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("catch2-devel")
def _devel(self):
    return self.default_devel()
