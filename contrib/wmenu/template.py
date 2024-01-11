pkgname = "wmenu"
pkgver = "0.1.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu for Wayland"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://sr.ht/~adnano/wmenu"
source = f"https://git.sr.ht/~adnano/wmenu/archive/{pkgver}.tar.gz"
sha256 = "e1346cfb54970f2f16e98ab1744dcc30ca506fd8224f64a8c7ef1602bc5eb7f9"


def post_install(self):
    self.install_license("LICENSE")
