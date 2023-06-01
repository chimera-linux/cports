pkgname = "python-cython"
pkgver = "0.29.35"
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
sha256 = "6e381fa0bf08b3c26ec2f616b19ae852c06f5750f4290118bf986b6f85c8c527"
# flaky tests
options = ["!check"]
