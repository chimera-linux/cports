pkgname = "python-flake8"
pkgver = "7.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pycodestyle", "python-pyflakes", "python-mccabe"]
checkdepends = ["python-pytest", "python-mock"] + depends
pkgdesc = "Python tool for style guide enforcement"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://flake8.pycqa.org"
source = f"https://github.com/PyCQA/flake8/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "af2223f8d6476097ac0bf58a08910fa19b4c045d37f6c8e26532d3f4076b78ba"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
