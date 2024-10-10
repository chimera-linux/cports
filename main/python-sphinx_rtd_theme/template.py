pkgname = "python-sphinx_rtd_theme"
pkgver = "3.0.1"
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
sha256 = "588b3d1448be4dece8d85bbdd8f0f7de703e8b49011e052d676c609dcd3374cd"
# No tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
