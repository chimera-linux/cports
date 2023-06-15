pkgname = "swaylock"
pkgver = "1.7.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-protocols"]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "wayland-devel",
]
pkgdesc = "Screen locker for Wayland"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT"
url = "https://github.com/swaywm/swaylock"
source = f"https://github.com/swaywm/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bf965d47fb6fc1402f854d4679d21a9459713fc0f330bc607c9585db097b4304"


def post_install(self):
    self.install_license("LICENSE")
