pkgname = "python-click"
pkgver = "8.2.2"
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
sha256 = "068616e6ef9705a07b6db727cb9c248f4eb9dae437a30239f56fa94b18b852ef"


def post_install(self):
    self.install_license("LICENSE.txt")
