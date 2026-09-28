pkgname = "swaybg"
pkgver = "1.2.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wallpaper tool for Wayland compositors"
license = "MIT"
url = "https://github.com/swaywm/swaybg"
source = f"{url}/releases/download/v{pkgver}/swaybg-{pkgver}.tar.gz"
sha256 = "a6652a0060a0bea3c3318d9d03b6dddac34f6aeca01b883eef9e58281f5202a1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
