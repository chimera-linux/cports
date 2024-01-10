pkgname = "python-flake8"
pkgver = "7.0.0"
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
sha256 = "9b649d29d4bc2562e2d814ffdc63b90828e3f43b50bc146021901b4446bae7fb"
# some failures in new testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
