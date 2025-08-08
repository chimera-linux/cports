pkgname = "python-txaio"
pkgver = "25.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python compatibility API between asyncio/Twisted"
license = "MIT"
url = "https://txaio.readthedocs.io"
source = f"$(PYPI_SITE)/t/txaio/txaio-{pkgver}.tar.gz"
sha256 = "d8c03dca823515c9bca920df33504923ae54f2dabf476cc5a9ed5cc1691ed687"
# Wants deprecated trollius
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
