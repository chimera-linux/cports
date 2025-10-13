pkgname = "python-cffi"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "libffi8-devel",
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["libffi8-devel", "python-devel"]
depends = ["python-pycparser"]
checkdepends = ["python-pycparser", "python-pytest"]
pkgdesc = "C FFI for Python"
license = "MIT"
url = "https://cffi.readthedocs.io"
source = f"$(PYPI_SITE)/c/cffi/cffi-{pkgver}.tar.gz"
sha256 = "44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529"
# tests crash on loongarch64
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE")
