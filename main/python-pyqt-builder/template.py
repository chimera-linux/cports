pkgname = "python-pyqt-builder"
pkgver = "1.17.1"
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
sha256 = "457dcd6a1408ea4bf1264e3511c734d53451ae8a3905e98982d50f7b3fdab724"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
