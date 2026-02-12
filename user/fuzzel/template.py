pkgname = "fuzzel"
pkgver = "1.14.0"
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
sha256 = "f46387b29e855990614c0b699fda99130d1406f65e5ea8b447c8f7ac4b64efe4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
