pkgname = "wl-kbptr"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Control the mouse pointer with the keyboard"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/moverest/wl-kbptr"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5d92d3217e7c77050fdd95f6602ffee3ae384f374400d95167adc721c37eba98"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
