pkgname = "python-pypng"
pkgver = "0.20220715.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for saving and loading PNG images"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://gitlab.com/drj11/pypng"
source = f"$(PYPI_SITE)/p/pypng/pypng-{pkgver}.tar.gz"
sha256 = "739c433ba96f078315de54c0db975aee537cbc3e1d0ae4ed9aab0ca1e427e2c1"
# broken tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
