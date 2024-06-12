pkgname = "python-websockets"
pkgver = "12.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Library for building WebSocket servers and clients in Python"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/python-websockets/websockets"
# pypi tarball doesn't ship tests
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "49978ae3f2aedf1c40ce9031c547fb766deaf7e86c3ec9677f0f5991bdc160ec"
# tests require a network connection :^)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
