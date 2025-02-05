pkgname = "iperf"
pkgver = "3.18"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "slibtool",
]
makedepends = ["openssl3-devel"]
pkgdesc = "IP bandwidth measurement tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause-LBNL"
url = "https://github.com/esnet/iperf"
source = f"https://github.com/esnet/iperf/releases/download/{pkgver}/iperf-{pkgver}.tar.gz"
sha256 = "c0618175514331e766522500e20c94bfb293b4424eb27d7207fb427b88d20bab"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("iperf-devel")
def _(self):
    return self.default_devel()
