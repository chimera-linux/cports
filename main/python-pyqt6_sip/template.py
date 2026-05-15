pkgname = "python-pyqt6_sip"
pkgver = "13.11.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "PyQt6 support for python-sip"
license = "custom:sip"
url = "https://www.riverbankcomputing.com/software/sip"
source = f"$(PYPI_SITE)/P/PyQt6_sip/pyqt6_sip-{pkgver}.tar.gz"
sha256 = "869c5b48afe38e55b1ee0dd72182b0886e968cc509b98023ff50010b013ce1be"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
