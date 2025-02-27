pkgname = "python-pyqt-builder"
pkgver = "1.18.1"
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
sha256 = "3f7a3a2715947a293a97530a76fd59f1309fcb8e57a5830f45c79fe7249b3998"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
