pkgname = "fasttext"
pkgver = "0.9.2"
pkgrel = 1
build_style = "cmake"
configure_args = [f"-DPROJECT_VERSION={pkgver}"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library for fast text representation and classification"
license = "MIT"
url = "https://fasttext.cc/index.html"
source = f"https://github.com/facebookresearch/fasttext/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7ea4edcdb64bfc6faaaec193ef181bdc108ee62bb6a04e48b2e80b639a99e27e"
# Tests require 300+MB test data downloaded with a script
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("fasttext-devel")
def _(self):
    return self.default_devel()
