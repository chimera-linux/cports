pkgname = "python-librt"
pkgver = "0.11.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Runtime library for mypyc"
license = "MIT"
url = "https://github.com/mypyc/librt"
source = f"$(PYPI_SITE)/l/librt/librt-{pkgver}.tar.gz"
sha256 = "075dc3ef4458a278e0195cbf6ac9d38808d9b906c5a6c7f7f79c3888276a3fb1"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
