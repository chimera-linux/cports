pkgname = "python-click"
pkgver = "8.1.7"
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
sha256 = "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"


def post_install(self):
    self.install_license("LICENSE.rst")
