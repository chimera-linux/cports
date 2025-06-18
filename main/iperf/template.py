pkgname = "iperf"
pkgver = "3.19"
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
sha256 = "da5cff29e4945b2ee05dcf9a0c67768cc000dc1b122935bce3492c4e36f6b5e9"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iperf-devel")
def _(self):
    return self.default_devel()
