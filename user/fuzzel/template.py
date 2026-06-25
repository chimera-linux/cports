pkgname = "fuzzel"
pkgver = "1.14.1"
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
    "libpng-devel",
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
sha256 = "c6416786c3a0600b8ad91ed951c43c002a639870c3823b4a60c910442f4ae097"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
