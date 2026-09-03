pkgname = "fuzzel"
pkgver = "1.15.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsvg-backend=resvg", "-Denable-cairo=disabled"]
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
    "linux-headers",
    "pixman-devel",
    "resvg-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Application launcher for wlroots-based Wayland compositors"
license = "MIT"
url = "https://codeberg.org/dnkl/fuzzel"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "95b6c022fc1f1c7ab586d47c1594417cc311bf41ea8f5f8b5641478da7b5cf3b"
hardening = ["vis", "cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
