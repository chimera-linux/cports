pkgname = "enet"
pkgver = "1.3.18"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "UDP networking library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "http://enet.bespin.org"
source = f"{url}/download/enet-{pkgver}.tar.gz"
sha256 = "2a8a0c5360d68bb4fcd11f2e4c47c69976e8d2c85b109dd7d60b1181a4f85d36"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("enet-devel")
def _(self):
    return self.default_devel()
