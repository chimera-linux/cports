pkgname = "openjph"
pkgver = "0.22.0"
pkgrel = 0
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
sha256 = "c9c6e9ec82ee8770ede41eeffe8acaab1814724c698b258c3de160dc09cb7d12"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openjph-devel")
def _(self):
    return self.default_devel()
