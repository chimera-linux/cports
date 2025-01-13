pkgname = "pugixml"
pkgver = "1.15"
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
sha256 = "b39647064d9e28297a34278bfb897092bf33b7c487906ddfc094c9e8868bddcb"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("pugixml-devel")
def _(self):
    return self.default_devel()
