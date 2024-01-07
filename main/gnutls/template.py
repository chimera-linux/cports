pkgname = "gnutls"
pkgver = "3.8.2"
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
    "nettle-devel",
    "libtasn1-devel",
    "libidn2-devel",
    "libgpg-error-devel",
    "libunistring-devel",
    "zlib-devel",
    "lzo-devel",
    "p11-kit-devel",
    "unbound-devel",
    "trousers-devel",
]
# dlopened
depends = ["libtspi"]
pkgdesc = "GNU Transport Layer Security library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e765e5016ffa9b9dd243e363a0460d577074444ee2491267db2e96c9c2adef77"


@subpackage("gnutls-devel")
def _devel(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("gnutls-progs")
def _progs(self):
    return self.default_progs()
