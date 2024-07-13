pkgname = "python-pyqt6_sip"
pkgver = "13.8.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://www.riverbankcomputing.com/software/sip"
source = f"$(PYPI_SITE)/P/PyQt6_sip/PyQt6_sip-{pkgver}.tar.gz"
sha256 = "2f74cf3d6d9cab5152bd9f49d570b2dfb87553ebb5c4919abfde27f5b9fd69d4"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
