pkgname = "swayidle"
pkgver = "1.9.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = ["elogind-devel", "wayland-devel", "wayland-protocols"]
pkgdesc = "Idle management daemon for Wayland"
license = "MIT"
url = "https://github.com/swaywm/swayidle"
source = f"{url}/releases/download/v{pkgver}/swayidle-{pkgver}.tar.gz"
sha256 = "6c1b769038b60250c88e47380cbb021cfa57a65f872bf4d6c340b5e3057096ac"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
