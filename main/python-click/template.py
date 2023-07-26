pkgname = "python-click"
pkgver = "8.1.6"
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
sha256 = "48ee849951919527a045bfe3bf7baa8a959c423134e1a5b98c05c20ba75a1cbd"


def post_install(self):
    self.install_license("LICENSE.rst")
