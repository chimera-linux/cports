pkgname = "python-pyqt-builder"
pkgver = "1.19.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python"]
pkgdesc = "PEP517 backend for PyQt projects"
license = "custom:sip"
url = "https://github.com/Python-PyQt/PyQt-builder"
source = f"$(PYPI_SITE)/P/PyQt-builder/pyqt_builder-{pkgver}.tar.gz"
sha256 = "6af6646ba29668751b039bfdced51642cb510e300796b58a4d68b7f956a024d8"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
