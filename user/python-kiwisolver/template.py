pkgname = "python-kiwisolver"
pkgver = "1.4.9"
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
sha256 = "c3b22c26c6fd6811b0ae8363b95ca8ce4ea3c202d3d0975b2914310ceb1bcc4d"


def post_install(self):
    self.install_license("LICENSE")
