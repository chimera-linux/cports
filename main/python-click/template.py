pkgname = "python-click"
pkgver = "8.1.5"
pkgrel = 0
build_style = "python_module"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for command line interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/click"
source = f"$(PYPI_SITE)/c/click/click-{pkgver}.tar.gz"
sha256 = "4be4b1af8d665c6d942909916d31a213a106800c47d0eeba73d34da3cbc11367"


def post_install(self):
    self.install_license("LICENSE.rst")
