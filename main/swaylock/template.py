pkgname = "swaylock"
pkgver = "1.8.3"
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
sha256 = "c9edc022cefc84d5762df9e480eed16627776897def52d630c0348de53f04f94"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
