pkgname = "python-attrs"
pkgver = "21.4.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"] # and other stuff, but does not matter
depends = ["python"]
pkgdesc = "Attributes without boilerplate"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://attrs.readthedocs.io"
source = f"$(PYPI_SITE)/a/attrs/attrs-{pkgver}.tar.gz"
sha256 = "626ba8234211db98e869df76230a137c4c40a12d72445c45d5f5b716f076e2fd"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
