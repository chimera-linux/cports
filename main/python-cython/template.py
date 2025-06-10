pkgname = "python-cython"
pkgver = "3.1.2"
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
sha256 = "6bbf7a953fa6762dfecdec015e3b054ba51c0121a45ad851fa130f63f5331381"
# check: flaky tests
options = ["!check"]
