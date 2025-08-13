pkgname = "python-nodeenv"
pkgver = "1.9.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
checkdepends = [
    "python-coverage",
    "python-pytest",
]
depends = [
    "nodejs",
    "python",
]
pkgdesc = "Tool to create isolated node.js environments"
license = "BSD-3-Clause"
url = "https://github.com/ekalinin/nodeenv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0d8ba86a1e4ab68bb16e8f1a1ac4f6261288012c72d4fa4a697949535c2c8d04"
# tests depend on tooling that we don't have yet (and that isn't easy to package)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
