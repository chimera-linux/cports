pkgname = "python-pyqt6_sip"
pkgver = "13.10.2"
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
sha256 = "464ad156bf526500ce6bd05cac7a82280af6309974d816739b4a9a627156fafe"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
