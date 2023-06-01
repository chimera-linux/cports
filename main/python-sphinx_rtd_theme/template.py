pkgname = "python-sphinx_rtd_theme"
pkgver = "1.2.0"
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
sha256 = "6f79aaccdf2a6019f6fb7486b22c2b3a37bd8571845ae3105b39486d8b77024e"
# No tests available
options = ["!check"]
