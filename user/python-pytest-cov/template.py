pkgname = "python-pytest-cov"
pkgver = "5.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = [
    "python-coverage",
    "python-pytest",
]
depends = [
    "python-coverage",
    "python-pytest",
]
pkgdesc = "Coverage reports for Pytest"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-cov"
source = f"$(PYPI_SITE)/p/pytest-cov/pytest-cov-{pkgver}.tar.gz"
sha256 = "5837b58e9f6ebd335b0f8060eecce69b662415b16dc503883a02f45dfeb14857"
# ModuleNotFoundError: No module named 'virtualenv'
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
