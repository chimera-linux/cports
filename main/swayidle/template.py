pkgname = "swayidle"
pkgver = "1.9.1"
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
sha256 = "6e1655ecba30db14de3df1652ef9dd1db72784946fa65cb222404a87ac825d57"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
