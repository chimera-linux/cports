pkgname = "python-click"
pkgver = "8.1.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for command line interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/click"
source = f"$(PYPI_SITE)/c/click/click-{pkgver}.tar.gz"
sha256 = "ed53c9d8990d83c2a27deae68e4ee337473f6330c040a31d4225c9574d16096a"


def post_install(self):
    self.install_license("LICENSE.txt")
