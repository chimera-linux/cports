pkgname = "libmicrohttpd"
pkgver = "1.0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-doc"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["gnutls-devel", "linux-headers"]
checkdepends = ["curl-devel"]
pkgdesc = "HTTP server library"
license = "LGPL-2.1-or-later"
url = "https://www.gnu.org/software/libmicrohttpd"
source = f"$(GNU_SITE)/libmicrohttpd/libmicrohttpd-{pkgver}.tar.gz"
sha256 = "df324fcd0834175dab07483133902d9774a605bfa298025f69883288fd20a8c7"


@subpackage("libmicrohttpd-devel")
def _(self):
    return self.default_devel()
