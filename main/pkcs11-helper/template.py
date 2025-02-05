pkgname = "pkcs11-helper"
pkgver = "1.30.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-slotevent",
    "--enable-threading",
]
hostmakedepends = ["automake", "pkgconf", "libtool"]
makedepends = ["openssl3-devel"]
pkgdesc = "Helper library for multiple PKCS#11 providers"
maintainer = "Dmitriy Vakhrushev <dvakhrushev@netgate.com>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://github.com/OpenSC/pkcs11-helper"
source = f"{url}/archive/refs/tags/pkcs11-helper-{pkgver}.tar.gz"
sha256 = "076c9f664812a45f2da25efc157338b0b8bb1949117f0144050fec176b6fdf78"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.BSD")


@subpackage("pkcs11-helper-devel")
def _(self):
    return self.default_devel()
