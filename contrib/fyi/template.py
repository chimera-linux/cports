pkgname = "fyi"
pkgver = "1.0.1"
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
sha256 = "1a189d09234ea8ed3a66e5946b6bb49c6a424aa21d99759a4c5830303dff68bf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
