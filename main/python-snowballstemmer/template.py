pkgname = "python-snowballstemmer"
pkgver = "3.0.1"
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
sha256 = "6d5eeeec8e9f84d4d56b847692bacf79bc2c8e90c7f80ca4444ff8b6f2e52895"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
