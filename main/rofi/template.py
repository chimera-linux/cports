pkgname = "rofi"
pkgver = "1.7.7_p1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["bison", "cmake", "meson", "ninja", "pkgconf"]
makedepends = [
    "cairo-devel",
    "flex",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "libjpeg-turbo-devel",
    "librsvg",
    "libx11-devel",
    "libxcb-devel",
    "libxft-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pango-devel",
    "startup-notification-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-imdkit-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Window switcher, run dialog, and dmenu replacement"
maintainer = "Nova <froggo8311@proton.me>"
license = "MIT"
# rofi with wayland support
url = "https://github.com/lbonn/rofi"
source = f"{url}/releases/download/{pkgver.replace('_p', '+wayland')}/rofi-{pkgver.replace('_p', '+wayland')}.tar.gz"
sha256 = "ef05c251c173172d58b90897c5dd3643da084963aaefff23c07bced7f325d5b7"


def post_install(self):
    self.install_license("COPYING")
