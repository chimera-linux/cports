pkgname = "python-pyqt-builder"
pkgver = "1.17.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "PEP517 backend for PyQt projects"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:sip"
url = "https://github.com/Python-PyQt/PyQt-builder"
source = f"$(PYPI_SITE)/P/PyQt-builder/pyqt_builder-{pkgver}.tar.gz"
sha256 = "cef9e06ab78c147235a5e4691e6257c963e93c2235fe3db1fe38c92f11977596"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
