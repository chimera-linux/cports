pkgname = "python-nftables"
pkgver = "1.1.0"
pkgrel = 0
build_wrksrc = "py"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["libnftables", "python"]
pkgdesc = "Python bindings for nftables"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND GPL-2.0-or-later"
url = "https://netfilter.org/projects/nftables"
source = f"{url}/files/nftables-{pkgver}.tar.xz"
sha256 = "ef3373294886c5b607ee7be82c56a25bc04e75f802f8e8adcd55aac91eb0aa24"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../COPYING")
