pkgname = "python-flake8"
pkgver = "7.3.0"
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
license = "MIT"
url = "https://flake8.pycqa.org"
source = f"https://github.com/PyCQA/flake8/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "71a7d2ec4166f83c6fc66e6465a45c49b4565ee29b69f27b335366ce101d8c2b"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
