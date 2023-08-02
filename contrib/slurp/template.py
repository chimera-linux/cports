pkgname = "slurp"
pkgver = "1.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Tool to select a region in a wayland compositor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/emersion/slurp"
source = f"{url}/releases/download/v{pkgver}/slurp-{pkgver}.tar.gz"
sha256 = "98f6bb692be6bd015aa6251830837ea4fd9a0c5d51ce832ad147aa62ae7f095d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
