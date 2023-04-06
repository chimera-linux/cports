pkgname = "python-cython"
pkgver = "0.29.34"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
makedepends = ["python-devel"]
depends = ["python", "python-setuptools"]
pkgdesc = "C extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://cython.org"
source = f"$(PYPI_SITE)/C/Cython/Cython-{pkgver}.tar.gz"
sha256 = "1909688f5d7b521a60c396d20bba9e47a1b2d2784bfb085401e1e1e7d29a29a8"
# flaky tests
options = ["!check"]
