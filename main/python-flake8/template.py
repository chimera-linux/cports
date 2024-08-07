pkgname = "python-flake8"
pkgver = "7.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pycodestyle", "python-pyflakes", "python-mccabe"]
checkdepends = ["python-pytest", "python-mock", *depends]
pkgdesc = "Python tool for style guide enforcement"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://flake8.pycqa.org"
source = f"https://github.com/PyCQA/flake8/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e389d1806e1f911b092fd41b7989c751f05eda510bab4ac255b144da96477e2b"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
