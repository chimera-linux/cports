pkgname = "fyi"
pkgver = "1.0.2"
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
sha256 = "a56a28146dc5751920505a53ee8124f0457358a6c88a99d2ad7e5ff79e9608fe"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
