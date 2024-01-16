pkgname = "swayidle"
pkgver = "1.8.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = ["elogind-devel", "wayland-devel", "wayland-protocols"]
pkgdesc = "Idle management daemon for Wayland"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/swaywm/swayidle"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "16b3e76a117f2f0ff2ee5fbebf38849595cdd705db1cd5f6aceaed00d71b3aa1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
