pkgname = "python-pyasn1_modules"
pkgver = "0.4.2"
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
license = "BSD-2-Clause"
url = "https://pyasn1.readthedocs.io/en/latest/contents.html"
source = f"$(PYPI_SITE)/p/pyasn1_modules/pyasn1_modules-{pkgver}.tar.gz"
sha256 = "677091de870a80aae844b1ca6134f54652fa2c8c5a52aa396440ac3106e941e6"


def post_install(self):
    self.install_license("LICENSE.txt")
