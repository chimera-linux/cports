pkgname = "iperf"
pkgver = "3.19.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "slibtool",
]
makedepends = ["openssl3-devel"]
pkgdesc = "IP bandwidth measurement tool"
license = "BSD-3-Clause-LBNL"
url = "https://github.com/esnet/iperf"
# source = f"{url}/releases/download/{pkgver}/iperf-{pkgver}.tar.gz"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "85e480d7fffdcb1368888aaee9d76bcfc211e17c2a6dcb2060b281498f82c97b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iperf-devel")
def _(self):
    return self.default_devel()
