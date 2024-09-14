pkgname = "ngtcp2"
pkgver = "1.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GNUTLS=ON"]
make_check_target = "check"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gnutls-devel"]
pkgdesc = "C IETF QUIC protocol implementation"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ngtcp2/ngtcp2"
source = f"{url}/releases/download/v{pkgver}/ngtcp2-{pkgver}.tar.xz"
sha256 = "e07c79090f96f6738fabab2129657c53f0cc05164de3662592581ca5425617b1"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _(self):
    return self.default_devel()
