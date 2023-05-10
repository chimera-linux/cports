pkgname = "python-pyasn1-modules"
pkgver = "0.2.8"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-pyasn1"]
checkdepends = ["python-pyasn1"]
pkgdesc = "Python ASN.1 protocol modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/etingof/pyasn1-modules"
source = f"$(PYPI_SITE)/p/pyasn1-modules/pyasn1-modules-{pkgver}.tar.gz"
sha256 = "905f84c712230b2c592c19470d3ca8d552de726050d1d1716282a1f6146be65e"

def post_install(self):
    self.install_license("LICENSE.txt")
