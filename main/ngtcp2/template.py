pkgname = "ngtcp2"
pkgver = "1.14.0"
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
sha256 = "d1fbf9eae92921bfd33154dab2574bc4b7d7936f486396d6c78bfff90ed5b35d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _(self):
    return self.default_devel()
