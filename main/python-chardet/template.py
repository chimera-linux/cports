pkgname = "python-chardet"
pkgver = "5.0.0"
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
sha256 = "0368df2bfd78b5fc20572bb4e9bb7fb53e2c094f60ae9993339e8671d0afb8aa"
# dependency of pytest
options = ["!check"]
