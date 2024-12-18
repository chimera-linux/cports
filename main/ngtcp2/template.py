pkgname = "ngtcp2"
pkgver = "1.9.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ngtcp2/ngtcp2"
source = f"{url}/releases/download/v{pkgver}/ngtcp2-{pkgver}.tar.xz"
sha256 = "f9617895c15d5d2985282aa948889d3ea032bf8a7db351d20cb9569352d64087"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _(self):
    return self.default_devel()
