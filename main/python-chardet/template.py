pkgname = "python-chardet"
pkgver = "4.0.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"]
depends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Universal encoding detector for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/chardet/chardet"
source = f"$(PYPI_SITE)/c/chardet/chardet-{pkgver}.tar.gz"
sha256 = "0d6f53a15db4120f2b08c94f11e7d93d2c911ee118b6b30a04ec3ee8310179fa"
# dependency of pytest
options = ["!check"]
