pkgname = "python-sphinx_rtd_theme"
pkgver = "1.2.2"
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
sha256 = "4e7034dfbf3861ec60ac1757b2e309538df038c82f81cc779a9dbd0fa8393cad"
# No tests available
options = ["!check"]
