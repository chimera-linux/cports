pkgname = "rofi"
pkgver = "1.7.8_p1"
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
sha256 = "45ec7c8e8484b2e18b9abeaf54fe1d64e7b7fe4fd1c589559a544dd3c81af7c8"


def post_install(self):
    self.install_license("COPYING")
