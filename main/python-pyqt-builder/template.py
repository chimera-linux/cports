pkgname = "python-pyqt-builder"
pkgver = "1.18.2"
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
sha256 = "56dfea461484a87a8f0c8b0229190defc436d7ec5de71102e20b35e5639180bc"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
