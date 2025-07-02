pkgname = "tayga"
pkgver = "0.9.5"
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
sha256 = "d44cc1158f60623d1bcd245f811957a162092c8f5e725489438de12e5500ae49"
# check: needs network namespaces
options = ["!check"]


def check(self):
    self.do("sh", "test/fullsuite.sh")


def install(self):
    self.install_bin("tayga")
    self.install_man("tayga.8")
    self.install_man("tayga.conf.5")
