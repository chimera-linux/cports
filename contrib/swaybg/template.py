pkgname = "swaybg"
pkgver = "1.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
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
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c0205b34f1fad94553b6cb2c2b983cc33186018026058cad0b841a00bc3087e3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
