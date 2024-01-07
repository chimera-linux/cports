pkgname = "python-pyserial"
pkgver = "3.5"
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
pkgdesc = "Python serial port module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/pyserial/pyserial"
source = f"$(PYPI_SITE)/p/pyserial/pyserial-{pkgver}.tar.gz"
sha256 = "3c77e014170dfffbd816e6ffc205e9842efb10be9f58ec16d3e8675b4925cddb"


def post_install(self):
    self.install_license("LICENSE.txt")
