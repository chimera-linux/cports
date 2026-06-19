pkgname = "ngtcp2"
pkgver = "1.23.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-gnutls", "--with-openssl"]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["gnutls-bootstrap", "openssl3-devel"]
pkgdesc = "C IETF QUIC protocol implementation"
license = "MIT"
url = "https://github.com/ngtcp2/ngtcp2"
source = f"{url}/releases/download/v{pkgver}/ngtcp2-{pkgver}.tar.xz"
sha256 = "59d5b4211e96970f2d3d5e6876f73dce03414800ba04aa56835b132fce8de730"


def post_install(self):
    self.install_license("COPYING")


@subpackage("ngtcp2-devel")
def _(self):
    return self.default_devel()


# projects explicitly link against crypto helpers of their choice
# so no install_if shenanigans or anything like that
@subpackage("ngtcp2-crypto-gnutls")
def _(self):
    self.subdesc = "GnuTLS helper"

    return ["usr/lib/libngtcp2_crypto_gnutls.so.*"]


@subpackage("ngtcp2-crypto-ossl")
def _(self):
    self.subdesc = "OpenSSL helper"

    return ["usr/lib/libngtcp2_crypto_ossl.so.*"]
