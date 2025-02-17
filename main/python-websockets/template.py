pkgname = "python-websockets"
pkgver = "15.0"
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
sha256 = "0c7d8599cf1ce596dad7fa939e8afd856b92f8d154989305123ee74fba906ced"
# tests require a network connection :^)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
