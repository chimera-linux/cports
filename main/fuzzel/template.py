pkgname = "fuzzel"
pkgver = "1.12.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsvg-backend=librsvg"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "fcft-devel",
    "fontconfig-devel",
    "freetype-devel",
    "librsvg-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pixman-devel",
    "tllist",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Application launcher for wlroots-based Wayland compositors"
license = "MIT"
url = "https://codeberg.org/dnkl/fuzzel"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "7f23b86d8fc635c368c69be7227aa7f8068a6ec7d07305a33c12db259400d3e8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
