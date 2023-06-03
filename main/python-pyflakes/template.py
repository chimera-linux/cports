pkgname = "python-pyflakes"
pkgver = "3.0.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python code linter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/pyflakes"
source = f"$(PYPI_SITE)/p/pyflakes/pyflakes-{pkgver}.tar.gz"
sha256 = "ec8b276a6b60bd80defed25add7e439881c19e64850afd9b346283d4165fd0fd"


def post_install(self):
    self.install_license("LICENSE")
