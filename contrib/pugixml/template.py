pkgname = "pugixml"
pkgver = "1.13"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DPUGIXML_BUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Light-weight, simple and fast XML parser for C++"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://pugixml.org"
source = f"https://github.com/zeux/pugixml/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5c5ad5d7caeb791420408042a7d88c2c6180781bf218feca259fd9d840a888e1"
# FIXME: cfi
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("pugixml-devel")
def _devel(self):
    return self.default_devel()
