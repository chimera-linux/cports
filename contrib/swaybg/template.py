pkgname = "swaybg"
pkgver = "1.2.1"
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
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/swaywm/swaybg"
source = f"{url}/releases/download/v{pkgver}/swaybg-{pkgver}.tar.gz"
sha256 = "6af1fdf0e57b1cc5345febed786b761fea0e170943a82639f94cfaed7df84f8f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
