pkgname = "python-nftables"
pkgver = "1.0.9"
pkgrel = 0
build_wrksrc = "py"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["libnftables"]
pkgdesc = "Python bindings for nftables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND GPL-2.0-or-later"
url = "https://netfilter.org/projects/nftables"
source = f"{url}/files/nftables-{pkgver}.tar.xz"
sha256 = "a3c304cd9ba061239ee0474f9afb938a9bb99d89b960246f66f0c3a0a85e14cd"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../COPYING")
