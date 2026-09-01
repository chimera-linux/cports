pkgname = "hyprgraphics"
pkgver = "0.5.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "file-devel",
    "hyprutils-devel",
    "libdrm-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "librsvg-devel",
    "libwebp-devel",
    "mesa-devel",
    "pango-devel",
    "pixman-devel",
]
checkdepends = [
    "fonts-dejavu-ttf",
]
pkgdesc = "Hyprland graphics resources and utilities"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprgraphics"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "861ecaad872835922dd5745a612d7a4cc7bfc4babb1d06bc92bc63c2ac013b74"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprgraphics-devel")
def _(self):
    return self.default_devel()
