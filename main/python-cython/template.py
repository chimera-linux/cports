pkgname = "python-cython"
pkgver = "0.29.24"
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
sha256 = "cdf04d07c3600860e8c2ebaad4e8f52ac3feb212453c1764a49ac08c827e8443"
# flaky tests
options = ["!check"]
