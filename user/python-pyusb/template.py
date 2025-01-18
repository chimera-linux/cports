pkgname = "python-pyusb"
pkgver = "1.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["libusb", "python"]
pkgdesc = "Easy USB access for Python"
maintainer = "Julie Koubova <julie@koubova.net>"
license = "BSD-3-Clause"
url = "https://github.com/pyusb/pyusb"
source = f"$(PYPI_SITE)/p/pyusb/pyusb-{pkgver}.tar.gz"
sha256 = "3af070b607467c1c164f49d5b0caabe8ac78dbed9298d703a8dbf9df4052d17e"
# no pytests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
