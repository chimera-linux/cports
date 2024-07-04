pkgname = "swaylock"
pkgver = "1.7.2"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Screen locker for Wayland"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/swaywm/swaylock"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bf965d47fb6fc1402f854d4679d21a9459713fc0f330bc607c9585db097b4304"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
