pkgname = "python-cffi"
pkgver = "1.17.0"
pkgrel = 0
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
sha256 = "f3157624b7558b914cb039fd1af735e5e8049a87c817cc215109ad1c8779df76"


def post_install(self):
    self.install_license("LICENSE")
