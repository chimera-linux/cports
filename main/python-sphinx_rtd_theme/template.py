pkgname = "python-sphinx_rtd_theme"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "python-sphinxcontrib-jquery"]
pkgdesc = "Sphinx theme for readthedocs.org"
license = "MIT"
url = "https://github.com/readthedocs/sphinx_rtd_theme"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f1755f1069616adacf1e00c0814e6b16192b7930ba4a3522993c3e096001b9b5"
# No tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
