pkgname = "python-click"
pkgver = "8.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["less", "python-pytest"]
pkgdesc = "Python module for command line interfaces"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/click"
source = f"$(PYPI_SITE)/c/click/click-{pkgver}.tar.gz"
sha256 = "27c491cc05d968d271d5a1db13e3b5a184636d9d930f148c50b038f0d0646202"


def post_install(self):
    self.install_license("LICENSE.txt")
