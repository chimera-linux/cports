pkgname = "python-kiwisolver"
pkgver = "1.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cppy",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
makedepends = [
    "python-devel",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Cassowary constraint solver"
license = "BSD-3-Clause"
url = "https://kiwisolver.readthedocs.io"
source = f"https://github.com/nucleic/kiwi/releases/download/{pkgver}/kiwisolver-{pkgver}.tar.gz"
sha256 = "d4193f3d9dc3f6f79aaed0e5637f45d98850ebf01f7ca20e69457f3e8946b66a"


def post_install(self):
    self.install_license("LICENSE")
