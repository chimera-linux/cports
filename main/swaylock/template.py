pkgname = "swaylock"
pkgver = "1.8.6"
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
sha256 = "a15154348fef852fdb224112d137c393c826478b777f63479beb15e8d3812eaf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
