pkgname = "python-pyqt-builder"
pkgver = "1.16.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
pkgdesc = "PEP517 backend for PyQt projects"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://www.riverbankcomputing.com/software/pyqt-builder"
source = f"$(PYPI_SITE)/P/PyQt-builder/PyQt-builder-{pkgver}.tar.gz"
sha256 = "47bbd2cfa5430020108f9f40301e166cbea98b6ef3e53953350bdd4c6b31ab18"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("pyqtbuild/bundle/qt_wheel_distinfo/LICENSE")
