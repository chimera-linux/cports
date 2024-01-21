pkgname = "python-fasttext"
pkgver = "0.9.2"
pkgrel = 0
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
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://fasttext.cc/index.html"
source = f"https://github.com/facebookresearch/fasttext/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7ea4edcdb64bfc6faaaec193ef181bdc108ee62bb6a04e48b2e80b639a99e27e"
# Tests require 300+MB test data downloaded with a script
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
