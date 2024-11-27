pkgname = "fuzzel"
pkgver = "1.11.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://codeberg.org/dnkl/fuzzel"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "7b22fefdada10e4658ec1f914a7296ddde73a5d20a2a1ed3c02c50bf2e701d3b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
