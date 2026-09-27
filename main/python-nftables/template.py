pkgname = "python-nftables"
pkgver = "1.1.7"
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
sha256 = "a6fbf060d8d4fff001517a2b94f356bb4366bfbf0ba366366f9d27cc38caa58f"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../COPYING")
