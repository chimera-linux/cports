pkgname = "python-gnupg"
pkgver = "0.5.4"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"NO_EXTERNAL_TESTS": "1"}
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = ["gnupg", "python"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python bindings for GnuPG"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "BSD-3-Clause"
url = "https://docs.red-dove.com/python-gnupg"
source = (
    f"https://github.com/vsajip/python-gnupg/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "d3c0b385ec07b7447622b920d43c0ed07a0323ab893e68752324c5735004c146"


def post_install(self):
    self.install_license("LICENSE.txt")
