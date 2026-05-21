pkgname = "libmicrohttpd"
pkgver = "1.0.5"
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
sha256 = "b46d00f58efa6f497b97d2e782c4ee66301d412ddd855dd3068518b3a2cd3ea2"


@subpackage("libmicrohttpd-devel")
def _(self):
    return self.default_devel()
