pkgname = "fuzzel"
pkgver = "1.10.2"
pkgrel = 2
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
sha256 = "5362175f301af3f27c23138ac339294ce33dff61720ffc7eb13e78ec56f60a8b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
