pkgname = "python-cffi"
pkgver = "1.16.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "libffi-devel",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["libffi-devel", "python-devel"]
depends = ["python-pycparser"]
checkdepends = ["python-pycparser", "python-pytest"]
pkgdesc = "C FFI for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://cffi.readthedocs.io"
source = f"$(PYPI_SITE)/c/cffi/cffi-{pkgver}.tar.gz"
sha256 = "bcb3ef43e58665bbda2fb198698fcae6776483e0c4a631aa5647806c25e02cc0"


def post_install(self):
    self.install_license("LICENSE")
