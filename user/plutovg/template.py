pkgname = "plutovg"
pkgver = "1.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DPLUTOVG_BUILD_EXAMPLES=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "linux-headers",
]
pkgdesc = "2D vector graphics library for C++"
license = "MIT"
url = "https://github.com/sammycage/plutovg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2b0d17a6e016f47b86f9c00e2cb82600041b1ea1f7d2a00c2d46ae542cbfed3c"


def post_install(self):
    self.install_license("LICENSE")


@split("devel")
def _(self):
    return self.default_devel()
