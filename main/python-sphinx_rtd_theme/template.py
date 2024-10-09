pkgname = "python-sphinx_rtd_theme"
pkgver = "3.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "python-sphinxcontrib-jquery"]
pkgdesc = "Sphinx theme for readthedocs.org"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://github.com/readthedocs/sphinx_rtd_theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6de403ec3f0a07de4728cf940d1a2c83fd92fa1786889b3617716774591032ef"
# No tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
