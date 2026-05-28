pkgname = "python-babel"
pkgver = "2.18.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "python-setuptools"]
pkgdesc = "Tools for internationalizing Python applications"
license = "BSD-3-Clause"
url = "https://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/babel-{pkgver}.tar.gz"
sha256 = "b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
