pkgname = "slurp"
pkgver = "1.5.0"
pkgrel = 1
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/emersion/slurp"
source = f"{url}/releases/download/v{pkgver}/slurp-{pkgver}.tar.gz"
sha256 = "eeb282b2adc8db5614b852596340b69da6f3954cf6cfbdc4392da509c934208a"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
