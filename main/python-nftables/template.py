pkgname = "python-nftables"
pkgver = "1.1.6"
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
sha256 = "372931bda8556b310636a2f9020adc710f9bab66f47efe0ce90bff800ac2530c"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../COPYING")
