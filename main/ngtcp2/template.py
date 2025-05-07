pkgname = "ngtcp2"
pkgver = "1.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GNUTLS=ON", "-DENABLE_OPENSSL=OFF"]
make_check_target = "check"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gnutls-devel"]
pkgdesc = "C IETF QUIC protocol implementation"
license = "MIT"
url = "https://github.com/ngtcp2/ngtcp2"
source = f"{url}/releases/download/v{pkgver}/ngtcp2-{pkgver}.tar.xz"
sha256 = "2527a4c9305dbed610a000a88f94696526aa8959f74249a59f2b96ee73630629"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _(self):
    return self.default_devel()
