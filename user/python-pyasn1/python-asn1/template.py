pkgname = "python-pyasn1"
pkgver = "0.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Generic ASN.1 library for Python"
license = "BSD-2-Clause"
url = "https://github.com/pyasn1/pyasn1"
source = f"$(PYPI_SITE)/p/pyasn1/pyasn1-{pkgver}.tar.gz"
sha256 = "6f580d2bdd84365380830acf45550f2511469f673cb4a5ae3857a3170128b034"


def post_install(self):
    self.install_license("LICENSE.rst")
