pkgname = "python-jsonlines"
pkgver = "4.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-attrs"]
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "Python library to simplify working with jsonlines and ndjson data"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://jsonlines.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/j/jsonlines/jsonlines-{pkgver}.tar.gz"
sha256 = "0c6d2c09117550c089995247f605ae4cf77dd1533041d366351f6f298822ea74"


def post_install(self):
    self.install_license("LICENSE.rst")
