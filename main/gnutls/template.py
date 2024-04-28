pkgname = "gnutls"
pkgver = "3.8.5"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-static",
    "--disable-valgrind-tests",
    "--enable-ktls",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
    "--with-zlib",
]
configure_gen = []
hostmakedepends = ["pkgconf", "gettext"]
makedepends = [
    "libgpg-error-devel",
    "libidn2-devel",
    "libtasn1-devel",
    "libunistring-devel",
    "linux-headers",
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
sha256 = "66269a2cfe0e1c2dabec87bdbbd8ab656f396edd9a40dd006978e003cfa52bfc"


@subpackage("gnutls-devel")
def _devel(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("gnutls-progs")
def _progs(self):
    return self.default_progs()
