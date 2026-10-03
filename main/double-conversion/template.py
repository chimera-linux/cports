pkgname = "double-conversion"
pkgver = "3.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTING=ON",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Efficient binary-decimal and decimal-binary routines for doubles"
license = "BSD-3-Clause"
url = "https://github.com/google/double-conversion"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "42fd4d980ea86426e457b24bdfa835a6f5ad9517ddb01cdb42b99ab9c8dd5dc9"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("double-conversion-devel")
def _(self):
    return self.default_devel()
