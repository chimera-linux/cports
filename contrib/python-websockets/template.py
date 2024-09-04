pkgname = "python-websockets"
pkgver = "13.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Library for building WebSocket servers and clients in Python"
maintainer = "c7s <c7s@kasku.net>"
license = "BSD-3-Clause"
url = "https://github.com/python-websockets/websockets"
# pypi tarball doesn't ship tests
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0cfb2f88ac0b693ed282d408479edc57b948e6a786c0d3e48222e4e8d6ade85d"
# tests require a network connection :^)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
