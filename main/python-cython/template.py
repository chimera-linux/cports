pkgname = "python-cython"
pkgver = "0.29.28"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
makedepends = ["python-devel"]
depends = ["python-setuptools"]
pkgdesc = "C extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://cython.org"
source = f"$(PYPI_SITE)/C/Cython/Cython-{pkgver}.tar.gz"
sha256 = "d6fac2342802c30e51426828fe084ff4deb1b3387367cf98976bb2e64b6f8e45"
# flaky tests
options = ["!check"]
