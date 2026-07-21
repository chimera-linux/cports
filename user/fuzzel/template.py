pkgname = "fuzzel"
pkgver = "1.14.1"
pkgrel = 1
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
sha256 = "4b8a914d7a065e34da7db4cc6ae4f02c773445e41b724b28b8b7385636b449ee"
hardening = ["vis", "cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
