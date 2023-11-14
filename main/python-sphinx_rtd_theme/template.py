pkgname = "python-sphinx_rtd_theme"
pkgver = "1.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-setuptools",
    "python-build",
    "python-installer",
    "python-wheel",
]
depends = ["python", "python-sphinxcontrib-jquery"]
pkgdesc = "Sphinx theme for readthedocs.org"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://github.com/readthedocs/sphinx_rtd_theme"
source = f"https://github.com/readthedocs/sphinx_rtd_theme/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "637611d42a95719235bf557567fadfea89d9e13c5e819f07640f74b75db90dd8"
# No tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
