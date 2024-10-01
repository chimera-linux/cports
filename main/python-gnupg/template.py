pkgname = "python-gnupg"
pkgver = "0.5.3"
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
sha256 = "f71114bcde8f4d66f41873d4f43a3dbc70b5b7d70869ecd0fdf97224405385fe"


def post_install(self):
    self.install_license("LICENSE.txt")
