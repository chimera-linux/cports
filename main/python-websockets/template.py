pkgname = "python-websockets"
pkgver = "14.1"
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
sha256 = "822f3c2bd7ac6b2d9b90271dccaf4e74453b3b0aba5323ade0bcade60102a5c1"
# tests require a network connection :^)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
