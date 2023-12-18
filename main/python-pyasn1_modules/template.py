pkgname = "python-pyasn1_modules"
pkgver = "0.3.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pyasn1"]
checkdepends = ["python-pytest", "python-pyasn1"]
pkgdesc = "Python ASN.1 protocol modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pyasn1.readthedocs.io/en/latest/contents.html"
source = f"$(PYPI_SITE)/p/pyasn1_modules/pyasn1_modules-{pkgver}.tar.gz"
sha256 = "5bd01446b736eb9d31512a30d46c1ac3395d676c6f3cafa4c03eb54b9925631c"


def post_install(self):
    self.install_license("LICENSE.txt")
