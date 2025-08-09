pkgname = "mew"
pkgver = "1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "fcft-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pkgconf",
    "wayland",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu for Wayland"
license = "MIT"
url = "https://codeberg.org/sewn/mew"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "01452fb92c6c5f792327ed8328bb2cbba55fa491260ccdf1b49db7960583c70b"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
