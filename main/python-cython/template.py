pkgname = "python-cython"
pkgver = "3.0.10"
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
sha256 = "dcc96739331fb854dcf503f94607576cfe8488066c61ca50dfd55836f132de99"
# flaky tests
options = ["!check"]
