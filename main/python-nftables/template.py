pkgname = "python-nftables"
pkgver = "1.1.1"
pkgrel = 1
build_wrksrc = "py"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["nftables-libs", "python"]
pkgdesc = "Python bindings for nftables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND GPL-2.0-or-later"
url = "https://netfilter.org/projects/nftables"
source = f"{url}/files/nftables-{pkgver}.tar.xz"
sha256 = "6358830f3a64f31e39b0ad421d7dadcd240b72343ded48d8ef13b8faf204865a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../COPYING")
