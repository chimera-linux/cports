pkgname = "python-cython"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "C extensions for Python"
license = "Apache-2.0"
url = "https://cython.org"
source = f"$(PYPI_SITE)/c/cython/cython-{pkgver}.tar.gz"
sha256 = "1097dd60d43ad0fff614a57524bfd531b35c13a907d13bee2cc2ec152e6bf4a1"
# check: flaky tests
options = ["!check"]
