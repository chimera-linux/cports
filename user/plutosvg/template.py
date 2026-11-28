pkgname = "plutosvg"
pkgver = "0.0.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DPLUTOSVG_BUILD_EXAMPLES=OFF",
    "-DPLUTOSVG_ENABLE_FREETYPE=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "freetype-devel",
    "plutovg-devel",
]
pkgdesc = "SVG rendering library in C"
license = "MIT"
url = "https://github.com/sammycage/plutosvg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "49d5cfe772d3aa10cd4879f2f6e189f5083c08e4c8ea01bf3d5b87c97dfca7d2"


def post_install(self):
    self.install_license("LICENSE")


@split("devel")
def _(self):
    return self.default_devel()
