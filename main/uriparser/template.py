pkgname = "uriparser"
pkgver = "0.9.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DURIPARSER_BUILD_DOCS=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtest-devel",
]
pkgdesc = "RFC 3986 compliant URI parsing and handling library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/uriparser/uriparser"
source = f"{url}/archive/refs/tags/uriparser-{pkgver}.tar.gz"
sha256 = "d6289387eaf2495e38ed80d709ad673fe04d63fad707badfee96f3d2dabc7c35"


def post_install(self):
    self.install_license("COPYING")


@subpackage("uriparser-devel")
def _(self):
    return self.default_devel()
