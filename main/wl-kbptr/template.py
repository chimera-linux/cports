pkgname = "wl-kbptr"
pkgver = "0.2.2"
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
sha256 = "d37524010f777eed0dd5a482b2b30737d8938bfd936140c666861ca212b25ebb"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("helpers/*", glob=True)
