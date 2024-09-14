pkgname = "fstrm"
pkgver = "0.6.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "libevent-devel",
]
pkgdesc = "C implementation of the Frame Streams data transport protocol"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/farsightsec/fstrm"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4f0f7ad2b760119c441aba58271e84de683b3cc138530d02710896641866e2d2"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fstrm-devel")
def _(self):
    return self.default_devel()
