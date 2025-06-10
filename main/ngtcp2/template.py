pkgname = "ngtcp2"
pkgver = "1.13.0"
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
sha256 = "cc98cdd7d0ce0050b5589c99f89ac72fb34aee6ff88bb3351f239407a65699fe"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _(self):
    return self.default_devel()
