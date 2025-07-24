pkgname = "python-kiwisolver"
pkgver = "1.4.8"
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
sha256 = "23d5f023bdc8c7e54eb65f03ca5d5bb25b601eac4d7f1a042888a1f45237987e"


def post_install(self):
    self.install_license("LICENSE")
