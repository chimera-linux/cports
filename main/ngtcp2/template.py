pkgname = "ngtcp2"
pkgver = "1.25.0"
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
sha256 = "2a34d2484ba17847a5d11965704e9dd0fac4c6d8efc75ffe1ec7de66d8c6b6fb"


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
