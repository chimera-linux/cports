pkgname = "neon"
pkgver = "0.34.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-expat",
    "--with-ssl",
    "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt",
    "--without-gssapi",
    "--enable-shared",
    "--enable-threadsafe-ssl=posix",
    "--disable-static",
    "--disable-nls",
]
configure_gen = ["./autogen.sh"]
make_dir = "."
make_check_args = ["-j1"]
hostmakedepends = [
    "automake",
    "libtool",
    "perl",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "libexpat-devel",
    "libproxy-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
depends = ["ca-certificates"]
pkgdesc = "HTTP and WebDAV client library"
license = "LGPL-2.0-or-later"
url = "https://notroj.github.io/neon"
source = f"{url}/neon-{pkgver}.tar.gz"
sha256 = "f98ce3c74300be05eddf05dccbdca498b14d40c289f773195dd1a559cffa5856"


@subpackage("neon-devel")
def _(self):
    return self.default_devel()
