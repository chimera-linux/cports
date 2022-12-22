pkgname = "gnutls"
pkgver = "3.7.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-zlib", "--disable-guile", "--disable-static",
    "--disable-valgrind-tests", "--disable-rpath",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
]
hostmakedepends = ["pkgconf", "gettext-tiny"]
makedepends = [
    "nettle-devel", "libtasn1-devel", "libidn2-devel", "libgpg-error-devel",
    "libunistring-devel", "zlib-devel", "lzo-devel", "p11-kit-devel",
    "unbound-devel", "trousers-devel",
]
# dlopened
depends = ["libtspi"]
pkgdesc = "GNU Transport Layer Security library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c58ad39af0670efe6a8aee5e3a8b2331a1200418b64b7c51977fb396d4617114"
# interactive
options = ["!check"]

@subpackage("gnutls-devel")
def _devel(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra = ["usr/share/info"])

@subpackage("gnutls-progs")
def _progs(self):
    return self.default_progs()

# FIXME visibility
hardening = ["!vis"]
