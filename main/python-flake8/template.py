pkgname = "python-flake8"
pkgver = "7.2.0"
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
sha256 = "a4e94891bcada0adf8b5bdf6be9f8a81bd09b0951674b52ca3e84f21ba0fe651"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
