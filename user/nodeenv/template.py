pkgname = "nodeenv"
pkgver = "1.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
depends = [
    "gmake",
    "nodejs",
    "python",
]
checkdepends = [
    "python-pytest",
    "python-pytest-mock",
    *depends,
]
pkgdesc = "Tool to create isolated node.js environments"
license = "BSD-3-Clause"
url = "https://github.com/ekalinin/nodeenv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5000579763a6e7f5e3d18ae8f69ae01b1b91ef2e4cb8b2d5d6a6f7f3e9a201b8"


def post_install(self):
    self.install_license("LICENSE")
