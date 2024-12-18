pkgname = "python-pyqt6_sip"
pkgver = "13.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "PyQt6 support for python-sip"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:sip"
url = "https://www.riverbankcomputing.com/software/sip"
source = f"$(PYPI_SITE)/P/PyQt6_sip/PyQt6_sip-{pkgver}.tar.gz"
sha256 = "5dc660f2242f6bd8c6bc5973a39f31a5b97f261f5ba69b4571912c7feae346bb"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
