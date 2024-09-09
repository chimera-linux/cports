pkgname = "fuzzel"
pkgver = "1.11.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://codeberg.org/dnkl/fuzzel"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4071728173dddac0df3d1b0af08ed92c4fdd4e86ff6bcf106d255a0acb67efdb"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
