pkgname = "tclap"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "pkgconf"]
pkgdesc = "Templatized command line argument parser"
license = "MIT"
url = "http://tclap.sourceforge.net"
source = (
    f"https://downloads.sourceforge.net/sourceforge/tclap/tclap-{pkgver}.tar.gz"
)
sha256 = "bb649f76dae35e8d0dcba4b52acfd4e062d787e6a81b43f7a4b01275153165a6"


def post_install(self):
    self.install_license("COPYING")
