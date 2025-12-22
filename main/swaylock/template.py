pkgname = "swaylock"
pkgver = "1.8.4"
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
license = "MIT"
url = "https://github.com/swaywm/swaylock"
source = f"{url}/releases/download/v{pkgver}/swaylock-{pkgver}.tar.gz"
sha256 = "aa251d5a8f335fe2ac9ec3cc2a6ac8772aa4dba2ec710ccd415956c6e89b11d3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
