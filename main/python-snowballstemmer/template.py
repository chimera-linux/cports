pkgname = "python-snowballstemmer"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Snowball stemming library collection for Python"
license = "BSD-3-Clause"
url = "https://snowballstem.org"
source = f"$(PYPI_SITE)/s/snowballstemmer/snowballstemmer-{pkgver}.tar.gz"
sha256 = "fd9e34526b23340cd23ffea6c9f9760974ecc2c2ac9e1d81401443ccdb2a801f"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
