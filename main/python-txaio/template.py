pkgname = "python-txaio"
pkgver = "23.1.1"
pkgrel = 1
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
sha256 = "f9a9216e976e5e3246dfd112ad7ad55ca915606b60b84a757ac769bd404ff704"
# Wants deprecated trollius
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
