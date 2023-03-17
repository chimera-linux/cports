pkgname = "python-attrs"
pkgver = "22.2.0"
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
sha256 = "c9227bfc2f01993c03f68db37d1d15c9690188323c067c641f1a35ca58185f99"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
