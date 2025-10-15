pkgname = "python-roman"
pkgver = "5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Integer to Roman numerals converter"
license = "ZPL-2.1"
url = "https://github.com/zopefoundation/roman"
source = f"$(PYPI_SITE)/r/roman/roman-{pkgver}.tar.gz"
sha256 = "3a86572e9bc9183e771769601189e5fa32f1620ffeceebb9eca836affb409986"
# not properly set up for tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
