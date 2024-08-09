pkgname = "fyi"
pkgver = "1.0.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["dbus-devel"]
pkgdesc = "Desktop notification sending utility"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/dnkl/fyi"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "39e563fc7db59608ffe8f34c96c04dbdce707ba4a8a97ed3300f03f50581ba66"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
