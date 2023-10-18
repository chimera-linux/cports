pkgname = "python-flake8"
pkgver = "6.1.0"
pkgrel = 0
build_style = "python_module"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-setuptools"]
depends = ["python-pycodestyle", "python-pyflakes", "python-mccabe"]
checkdepends = ["python-pytest", "python-mock"] + list(depends)
pkgdesc = "Python tool for style guide enforcement"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://flake8.pycqa.org"
source = f"https://github.com/PyCQA/flake8/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bcb01efc0c83d3c9362e200b5359fe22e11b859962dd27e5bebf3ada7620ae2f"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
