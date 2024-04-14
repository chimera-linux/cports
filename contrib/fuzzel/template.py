pkgname = "fuzzel"
pkgver = "1.10.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "fcft-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libxkbcommon-devel",
    "pixman-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Application launcher for wlroots-based Wayland compositors"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/dnkl/fuzzel"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "e89bf8395d92aa0975e6487049c47e44e40ebf0997dc493a8bb03ec465f1910a"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
