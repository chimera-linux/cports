pkgname = "mew"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "fcft-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu for Wayland"
license = "MIT"
url = "https://codeberg.org/sewn/mew"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9076073b1973330563b344034f152b855f3936ecebb1ad849ae5f3deb8fa5e0a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
