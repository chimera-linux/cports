pkgname = "python-vulture"
pkgver = "2.14"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
    "python-pint",
]
pkgdesc = "Find dead python code"
license = "MIT"
url = "https://github.com/jendrikseipp/vulture"
source = f"$(PYPI_SITE)/v/vulture/vulture-{pkgver}.tar.gz"
sha256 = "cb8277902a1138deeab796ec5bef7076a6e0248ca3607a3f3dee0b6d9e9b8415"


def post_install(self):
    self.install_license("LICENSE.txt")
