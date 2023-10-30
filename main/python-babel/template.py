pkgname = "python-babel"
pkgver = "2.13.1"
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
url = "http://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/Babel-{pkgver}.tar.gz"
sha256 = "33e0952d7dd6374af8dbf6768cc4ddf3ccfefc244f9986d4074704f2fbd18900"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
