pkgname = "wl-kbptr"
pkgver = "0.2.3"
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
sha256 = "0d03f83d94b6acfdb07f3ee3760c1abc207eef5a8346af38978d6bcb46ac58b8"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_bin("helpers/*", glob=True)
