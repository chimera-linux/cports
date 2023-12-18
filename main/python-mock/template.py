pkgname = "python-mock"
pkgver = "5.1.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python mock library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://mock.readthedocs.org"
source = f"$(PYPI_SITE)/m/mock/mock-{pkgver}.tar.gz"
sha256 = "5e96aad5ccda4718e0a229ed94b2024df75cc2d55575ba5762d31f5767b8767d"


def post_install(self):
    self.install_license("LICENSE.txt")
