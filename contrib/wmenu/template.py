pkgname = "wmenu"
pkgver = "0.1.6"
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
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Dynamic menu for wlroots compositors"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://git.sr.ht/~adnano/wmenu"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "0684739e6339ffad6562338a4bf67e29bf18688d1a9b0ddf31b693a64d29efac"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
