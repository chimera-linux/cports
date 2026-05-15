pkgname = "python-cython"
pkgver = "3.2.4"
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
sha256 = "84226ecd313b233da27dc2eb3601b4f222b8209c3a7216d8733b031da1dc64e6"
# check: flaky tests
options = ["!check"]
