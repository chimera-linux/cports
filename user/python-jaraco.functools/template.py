pkgname = "python-jaraco.functools"
pkgver = "4.1.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--deselect=test_functools.py"]  # unpackaged deps
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-more-itertools"]
checkdepends = [
    "python-pytest",
    "python-jaraco.classes",
    *depends,
]
pkgdesc = "Functools like those found in stdlib"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/jaraco.functools"
source = f"$(PYPI_SITE)/j/jaraco_functools/jaraco_functools-{pkgver}.tar.gz"
sha256 = "70f7e0e2ae076498e212562325e805204fc092d7b4c17e0e86c959e249701a9d"


def post_install(self):
    self.install_license("LICENSE")
