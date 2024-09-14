pkgname = "swaylock"
pkgver = "1.8.0"
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
    "libxkbcommon-devel",
    "linux-pam-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Screen locker for Wayland"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/swaywm/swaylock"
source = f"{url}/releases/download/v{pkgver}/swaylock-{pkgver}.tar.gz"
sha256 = "6a1175442380b87b2d2868c4a5366ee3592163158d02e3a7fbf3a0bfe07d8b00"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
