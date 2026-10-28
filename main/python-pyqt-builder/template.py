pkgname = "python-pyqt-builder"
pkgver = "1.20.3"
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
sha256 = "be65ff822a75d020fafc0edcaf9fd79b7e3f145a00995a177c98c3286a5f85d5"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
