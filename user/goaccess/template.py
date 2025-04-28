pkgname = "goaccess"
pkgver = "1.9.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8", "--enable-geoip=mmdb"]
hostmakedepends = ["automake", "gettext-devel"]
makedepends = ["libmaxminddb-devel", "ncurses-devel"]
pkgdesc = "Web log analyzer and interactive viewer"
license = "MIT"
url = "https://github.com/allinurl/goaccess"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "39be83ae8635364b421bd811ee36906360d0c4e86456a332c37f4205f456a543"


def post_install(self):
    self.install_license("COPYING")
