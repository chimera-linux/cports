pkgname = "mangowc"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"

hostmakedepends = ["meson", "pkgconf", "wayland-progs", "wayland-protocols"]

makedepends = [
    "hwdata-devel",
    "libdisplay-info-devel",
    "libinput-devel",
    "libliftoff-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pcre2-devel",
    "pixman-devel",
    "scenefx-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]

pkgdesc = "Wayland compositor based on wlroots and scenefx"
license = "MIT"
url = "https://github.com/dreammaomao/mangowc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1b1422dd73564302800720cc49aeb854e0a849696b822ba54b8f49dd63d32949"


def post_install(self):
    self.install_license("LICENSE")
