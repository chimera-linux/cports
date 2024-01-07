pkgname = "python-chardet"
pkgver = "5.2.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Universal encoding detector for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/chardet/chardet"
source = f"$(PYPI_SITE)/c/chardet/chardet-{pkgver}.tar.gz"
sha256 = "1b3b6ff479a8c414bc3fa2c0852995695c4a026dcd6d0633b2dd092ca39c1cf7"
# dependency of pytest
options = ["!check"]
