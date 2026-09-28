pkgname = "openjph"
pkgver = "0.25.0"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Implementation of JPEG2000 Part-15"
license = "BSD-2-Clause"
url = "https://github.com/aous72/OpenJPH"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "376fe46b8234e48eff0d26ce0bb9d0ee73aab5714a8b72a31d73d166b75aa62a"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openjph-devel")
def _(self):
    return self.default_devel()
