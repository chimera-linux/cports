pkgname = "python-click"
pkgver = "8.1.3"
pkgrel = 0
build_style = "python_module"
make_check_target = ""
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for command line interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/click"
source = f"$(PYPI_SITE)/c/click/click-{pkgver}.tar.gz"
sha256 = "7682dc8afb30297001674575ea00d1814d808d6a36af415a82bd481d37ba7b8e"


def post_install(self):
    self.install_license("LICENSE.rst")
