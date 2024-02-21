pkgname = "python-cython"
pkgver = "3.0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python", "python-setuptools"]
pkgdesc = "C extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://cython.org"
source = f"$(PYPI_SITE)/C/Cython/Cython-{pkgver}.tar.gz"
sha256 = "8333423d8fd5765e7cceea3a9985dd1e0a5dfeb2734629e1a2ed2d6233d39de6"
# flaky tests
options = ["!check"]
