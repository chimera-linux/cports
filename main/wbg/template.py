pkgname = "wbg"
pkgver = "1.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "libwebp-devel",
    "pixman-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wallpaper application for Wayland compositors"
license = "MIT"
url = "https://codeberg.org/dnkl/wbg"
source = f"{url}/releases/download/{pkgver}/wbg-{pkgver}.tar.gz"
sha256 = "5e23555c599e58f8fc76f2f8a697149c9fe96702a337a3e0457d503becb307a5"


def post_install(self):
    self.install_license("LICENSE")
