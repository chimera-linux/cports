pkgname = "python-sphinx_rtd_theme"
pkgver = "3.0.2"
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
sha256 = "6d8e0435e525afe04cb3a10e9429cff37febef612a376576b69b63178f289aba"
# No tests available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
