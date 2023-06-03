pkgname = "python-pycodestyle"
pkgver = "2.10.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python style guide checker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/pycodestyle"
source = f"$(PYPI_SITE)/p/pycodestyle/pycodestyle-{pkgver}.tar.gz"
sha256 = "347187bdb476329d98f695c213d7295a846d1152ff4fe9bacb8a9590b8ee7053"


def post_install(self):
    self.install_license("LICENSE")
