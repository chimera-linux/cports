pkgname = "wbg"
pkgver = "1.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "pixman-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wallpaper application for Wayland compositors"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "MIT"
url = "https://codeberg.org/dnkl/wbg"
source = f"{url}/releases/download/{pkgver}/wbg-{pkgver}.tar.gz"
sha256 = "a176576f3ca8d0494a5ce60a06970c093dcb46020ca678e5a327034ad8477a5e"


def post_install(self):
    self.install_license("LICENSE")
