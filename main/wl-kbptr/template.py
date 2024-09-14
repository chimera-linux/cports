pkgname = "wl-kbptr"
pkgver = "0.2.1"
pkgrel = 2
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
sha256 = "c014d8c12613b6267067cacf3f8737acc66514f18c1474de55d3cb3498c96bbe"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("helpers/*", glob=True)
