# XXX: don't update to 0.5.x unless python-pyasn1-modules is compatible
pkgname = "python-pyasn1"
pkgver = "0.4.8"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Python ASN.1 library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/etingof/pyasn1"
source = f"$(PYPI_SITE)/p/pyasn1/pyasn1-{pkgver}.tar.gz"
sha256 = "aef77c9fb94a3ac588e87841208bdec464471d9871bd5050a287cc9a475cd0ba"

def post_install(self):
    self.install_license("LICENSE.rst")
