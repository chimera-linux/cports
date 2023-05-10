pkgname = "python-pyasn1"
pkgver = "0.5.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Python ASN.1 library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pyasn1.readthedocs.io/en/latest/contents.html"
source = f"$(PYPI_SITE)/p/pyasn1/pyasn1-{pkgver}.tar.gz"
sha256 = "97b7290ca68e62a832558ec3976f15cbf911bf5d7c7039d8b861c2a0ece69fde"

def post_install(self):
    self.install_license("LICENSE.rst")
