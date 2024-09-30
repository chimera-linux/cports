pkgname = "python-pyasn1_modules"
pkgver = "0.4.1"
pkgrel = 0
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
sha256 = "c28e2dbf9c06ad61c71a075c7e0f9fd0f1b0bb2d2ad4377f240d33ac2ab60a7c"


def post_install(self):
    self.install_license("LICENSE.txt")
