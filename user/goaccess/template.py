pkgname = "goaccess"
pkgver = "1.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8", "--enable-geoip=mmdb", "--with-zlib"]
hostmakedepends = ["automake", "gettext-devel"]
makedepends = ["libmaxminddb-devel", "ncurses-devel", "zlib-ng-compat-devel"]
pkgdesc = "Web log analyzer and interactive viewer"
license = "MIT"
url = "https://github.com/allinurl/goaccess"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e0dc009cb2faf3cf6a3933060b9e593fd760a97d5c2294ee05fdf08f03e67e30"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")
