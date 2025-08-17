pkgname = "python-fasttext"
pkgver = "0.9.3"
pkgrel = 3
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-numpy",
    "python-pybind11",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["fasttext-devel"]
depends = ["python-numpy"]
pkgdesc = "Python bindings for fasttext"
license = "MIT"
url = "https://fasttext.cc/index.html"
source = f"$(PYPI_SITE)/f/fasttext/fasttext-{pkgver}.tar.gz"
sha256 = "eb03f2ef6340c6ac9e4398a30026f05471da99381b307aafe2f56e4cd26baaef"
# Tests require 300+MB test data downloaded with a script
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
