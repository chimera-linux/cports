pkgname = "catch2"
pkgver = "3.5.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCATCH_BUILD_TESTING=ON",
    "-DCATCH_BUILD_EXAMPLES=OFF",
    "-DCATCH_BUILD_EXTRA_TESTS=OFF",
    "-DCATCH_ENABLE_COVERAGE=OFF",
    "-DCATCH_INSTALL_DOCS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Modern, C++-native, unit test framework"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "BSL-1.0"
url = "https://github.com/catchorg/Catch2"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "269543a49eb76f40b3f93ff231d4c24c27a7e16c90e47d2e45bcc564de470c6e"
options = ["!lintstatic", "!lto"]


def post_install(self):
    self.install_license("LICENSE.txt")
