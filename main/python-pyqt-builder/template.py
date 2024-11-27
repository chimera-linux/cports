pkgname = "python-pyqt-builder"
pkgver = "1.16.4"
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
sha256 = "4515e41ae379be2e54f88a89ecf47cd6e4cac43e862c4abfde18389c2666afdf"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("pyqtbuild/bundle/qt_wheel_distinfo/LICENSE")
