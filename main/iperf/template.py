pkgname = "iperf"
pkgver = "3.17.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
]
makedepends = ["openssl-devel"]
pkgdesc = "IP bandwidth measurement tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause-LBNL"
url = "https://github.com/esnet/iperf"
source = f"https://github.com/esnet/iperf/releases/download/{pkgver}/iperf-{pkgver}.tar.gz"
sha256 = "84404ca8431b595e86c473d8f23d8bb102810001f15feaf610effd3b318788aa"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iperf-devel")
def _(self):
    return self.default_devel()
