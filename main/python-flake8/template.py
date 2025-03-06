pkgname = "python-flake8"
pkgver = "7.1.2"
pkgrel = 1
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
license = "MIT"
url = "https://flake8.pycqa.org"
source = f"https://github.com/PyCQA/flake8/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "60364d3593a8fd8a22f3ffcd751b29d0b61945e975754115bb9316bef157e03e"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
