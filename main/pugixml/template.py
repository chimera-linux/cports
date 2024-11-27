pkgname = "pugixml"
pkgver = "1.14"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://pugixml.org"
source = f"https://github.com/zeux/pugixml/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "610f98375424b5614754a6f34a491adbddaaec074e9044577d965160ec103d2e"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("pugixml-devel")
def _(self):
    return self.default_devel()
