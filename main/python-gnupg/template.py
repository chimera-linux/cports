pkgname = "python-gnupg"
pkgver = "0.5.5"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"NO_EXTERNAL_TESTS": "1"}
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = ["gnupg", "python"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python bindings for GnuPG"
license = "BSD-3-Clause"
url = "https://docs.red-dove.com/python-gnupg"
source = (
    f"https://github.com/vsajip/python-gnupg/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "c87d223fad6dca55a6006a38bc43142fea274c832730c00eac71421c5b4c06ec"


def post_install(self):
    self.install_license("LICENSE.txt")
