pkgname = "python-pyqt6_sip"
pkgver = "13.13.1"
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
sha256 = "83c3c9cb93b6c631af7048084fb0f234b610a01edbf9b2b44c4ee4bda4197efe"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
