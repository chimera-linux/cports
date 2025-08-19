pkgname = "fuzzel"
pkgver = "1.13.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsvg-backend=librsvg"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "fcft-devel",
    "fontconfig-devel",
    "freetype-devel",
    "librsvg-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pixman-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Application launcher for wlroots-based Wayland compositors"
license = "MIT"
url = "https://codeberg.org/dnkl/fuzzel"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "17e8f01753469573965a2a37b5745d03e6f6e7bda9d675cd2bc4644abb42d818"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
