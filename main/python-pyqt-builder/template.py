pkgname = "python-pyqt-builder"
pkgver = "1.18.0"
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
sha256 = "ce9930aafc1ce0af928a6944bcc80ecf78c23ffdcad6ac111306c4c71057848e"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
