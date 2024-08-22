pkgname = "mypaint-brushes"
pkgver = "2.0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "pkgconf"]
pkgdesc = "Brushes for libmypaint"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC0-1.0"
url = "https://github.com/mypaint/mypaint-brushes"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "01032550dd817bb0f8e85d83a632ed2e50bc16e0735630839e6c508f02f800ac"


def post_install(self):
    self.install_license("COPYING")
