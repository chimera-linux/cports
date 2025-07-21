pkgname = "rofi"
pkgver = "1.7.9_p1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["bison", "meson", "pkgconf"]
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
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Window switcher, run dialog, and dmenu replacement"
license = "MIT"
# rofi with wayland support
url = "https://github.com/lbonn/rofi"
source = f"{url}/releases/download/{pkgver.replace('_p', '+wayland')}/rofi-{pkgver.replace('_p', '+wayland')}.tar.gz"
sha256 = "688c5f477ad2ddb144b66786f9c188b6bf48f1e1bec38f7977aef94ed267d90f"


def post_install(self):
    self.install_license("COPYING")
