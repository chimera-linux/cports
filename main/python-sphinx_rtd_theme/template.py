pkgname = "python-sphinx_rtd_theme"
pkgver = "1.2.1"
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
sha256 = "b0b66baaee635120a67e66888b018d9d4ebb439ca6dfcf1e045d1fc30ba171a3"
# No tests available
options = ["!check"]
