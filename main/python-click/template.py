pkgname = "python-click"
pkgver = "8.1.4"
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
sha256 = "b97d0c74955da062a7d4ef92fadb583806a585b2ea81958a81bd72726cbb8e37"


def post_install(self):
    self.install_license("LICENSE.rst")
