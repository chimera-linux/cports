pkgname = "python-mpd2"
pkgver = "3.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Python client interface for MPD"
license = "LGPL-3.0-only"
url = "https://github.com/Mic92/python-mpd2"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8db24c423381625d6ae91aeb19de668e8d0c2a55f2f4c6b19b7775f4323d9123"
# skip tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
