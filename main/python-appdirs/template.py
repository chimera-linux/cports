pkgname = "python-appdirs"
pkgver = "1.4.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Platform-specific directory module for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ActiveState/appdirs"
source = f"$(PYPI_SITE)/a/appdirs/appdirs-{pkgver}.tar.gz"
sha256 = "7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41"


def post_install(self):
    self.install_license("LICENSE.txt")
