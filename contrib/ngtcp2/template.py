pkgname = "ngtcp2"
pkgver = "1.6.0"
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
source = f"https://github.com/ngtcp2/ngtcp2/releases/download/v{pkgver}/ngtcp2-{pkgver}.tar.xz"
sha256 = "2e575a42d369c2c982a1117f062ff9743fa07f87738ac5cedb304aa72260023a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _devel(self):
    return self.default_devel()
