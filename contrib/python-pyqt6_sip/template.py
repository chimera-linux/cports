pkgname = "python-pyqt6_sip"
pkgver = "13.6.0"
pkgrel = 1
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
sha256 = "2486e1588071943d4f6657ba09096dc9fffd2322ad2c30041e78ea3f037b5778"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
