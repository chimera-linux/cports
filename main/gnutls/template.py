pkgname = "gnutls"
pkgver = "3.8.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-static",
    "--disable-valgrind-tests",
    "--disable-afalg",  # broken outside x86_64
    "--enable-ktls",
    "--with-brotli=link",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
    "--with-tpm2=link",
    "--with-zlib=link",
    "--with-zstd=link",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "trousers-devel",
]
makedepends = [
    "brotli-devel",
    "gmp-devel",
    "libidn2-devel",
    "libtasn1-devel",
    "libunistring-devel",
    "linux-headers",
    "nettle-devel",
    "p11-kit-devel",
    "tpm2-tss-devel",
    "trousers-devel",
    "unbound-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# dlopened
depends = ["trousers-libs"]
pkgdesc = "GNU Transport Layer Security library"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/gnutls/v{'.'.join(pkgver.split('.')[0:2])}/gnutls-{pkgver}.tar.xz"
sha256 = "69e113d802d1670c4d5ac1b99040b1f2d5c7c05daec5003813c049b5184820ed"


def post_install(self):
    self.install_file(self.files_path / "config", "etc/gnutls")


@subpackage("gnutls-devel")
def _(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("gnutls-progs")
def _(self):
    return self.default_progs()
