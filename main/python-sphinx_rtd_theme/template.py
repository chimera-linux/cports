pkgname = "python-sphinx_rtd_theme"
pkgver = "2.0.0"
pkgrel = 1
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
sha256 = "40446e6789dd34deb4e9814e379bae0aa74057b6fb43de4b343a48c84fc0f8db"
# No tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
