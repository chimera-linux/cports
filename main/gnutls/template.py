pkgname = "gnutls"
pkgver = "3.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-zlib",
    "--disable-guile",
    "--disable-static",
    "--disable-valgrind-tests",
    "--disable-rpath",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
]
configure_gen = []
hostmakedepends = ["pkgconf", "gettext"]
makedepends = [
    "libgpg-error-devel",
    "libidn2-devel",
    "libtasn1-devel",
    "libunistring-devel",
    "lzo-devel",
    "nettle-devel",
    "p11-kit-devel",
    "trousers-devel",
    "unbound-devel",
    "zlib-devel",
]
# dlopened
depends = ["libtspi"]
pkgdesc = "GNU Transport Layer Security library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2bea4e154794f3f00180fa2a5c51fe8b005ac7a31cd58bd44cdfa7f36ebc3a9b"


@subpackage("gnutls-devel")
def _devel(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("gnutls-progs")
def _progs(self):
    return self.default_progs()
