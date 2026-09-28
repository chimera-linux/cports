pkgname = "gnutls-bootstrap"
pkgver = "3.8.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-libdane",
    "--disable-rpath",
    "--disable-static",
    "--disable-valgrind-tests",
    "--disable-afalg",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
    "--with-zlib=link",
    "--with-zstd=link",
    "--without-brotli",
    "--without-p11-kit",
    "--without-tpm2",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gmp-devel",
    "libidn2-devel",
    "libtasn1-devel",
    "libunistring-devel",
    "linux-headers",
    "nettle-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["texinfo"]
provides = [
    "pc:gnutls=3.8.0",
    "so:libgnutls.so.30=0",
    "so:libgnutlsxx.so.30=0",
]
pkgdesc = "GNU Transport Layer Security library"
subdesc = "bootstrap version"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/gnutls/v{'.'.join(pkgver.split('.')[0:2])}/gnutls-{pkgver}.tar.xz"
sha256 = "ffed8ec1bf09c2426d4f14aae377de4753b53e537d685e604e99a8b16ca9c97e"
options = ["!scanshlibs", "!scanpkgconf", "!autosplit"]


def post_install(self):
    self.uninstall("usr/bin")
