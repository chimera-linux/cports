pkgname = "python-log-symbols"
pkgver = "0.0.14"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Colored symbols for various log levels for Python"
maintainer = "Julie Koubova <julie@koubova.net>"
license = "MIT"
url = "https://github.com/manrajgrover/py-log-symbols"
source = f"$(PYPI_SITE)/l/log-symbols/log_symbols-{pkgver}.tar.gz"
sha256 = "cf0bbc6fe1a8e53f0d174a716bc625c4f87043cc21eb55dd8a740cfe22680556"
# missing nose, coverage
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
