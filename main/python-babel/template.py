pkgname = "python-babel"
pkgver = "2.16.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-setuptools"]
pkgdesc = "Tools for internationalizing Python applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/babel-{pkgver}.tar.gz"
sha256 = "d1f3554ca26605fe173f3de0c65f750f5a42f924499bf134de6423582298e316"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
