pkgname = "python-nftables"
pkgver = "1.1.3"
pkgrel = 0
build_wrksrc = "py"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["nftables-libs", "python"]
pkgdesc = "Python bindings for nftables"
license = "GPL-2.0-only AND GPL-2.0-or-later"
url = "https://netfilter.org/projects/nftables"
source = f"{url}/files/nftables-{pkgver}.tar.xz"
sha256 = "9c8a64b59c90b0825e540a9b8fcb9d2d942c636f81ba50199f068fde44f34ed8"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../COPYING")
