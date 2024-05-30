pkgname = "python-babel"
pkgver = "2.15.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytz"]
depends = ["python", "python-setuptools", "python-pytz"]
pkgdesc = "Tools for internationalizing Python applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/babel-{pkgver}.tar.gz"
sha256 = "8daf0e265d05768bc6c7a314cf1321e9a123afc328cc635c18622a2f30a04413"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
