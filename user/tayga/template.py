pkgname = "tayga"
pkgver = "0.9.6"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
checkdepends = [
    "iproute2",
    "python",
]
pkgdesc = "Out-of-kernel stateless NAT64 implementation"
license = "GPL-2.0-or-later"
url = "https://github.com/apalrd/tayga"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "64da04887e59207be0f62082e63dca98b1e770283fa37102ccb0a3e8d2acedc5"
# check: needs network namespaces
options = ["!check"]


def check(self):
    self.do("sh", "test/fullsuite.sh")


def install(self):
    self.install_bin("tayga")
    self.install_man("tayga.8")
    self.install_man("tayga.conf.5")
