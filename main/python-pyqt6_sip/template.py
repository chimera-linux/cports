pkgname = "python-pyqt6_sip"
pkgver = "13.13.0"
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
sha256 = "2cd55f575cde208c398d6cfdecc5a13394ed2afb54226210c50e3a6df7c3a997"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
