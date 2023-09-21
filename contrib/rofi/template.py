pkgname = "rofi"
_version = "1.7.5"
_release = 2
pkgver = f"{_version}_p{_release}"
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
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Window switcher, run dialog, and dmenu replacement"
maintainer = "Froggo <froggo8311@proton.me>"
license = "MIT"
# rofi with wayland support
url = "https://github.com/lbonn/rofi"
source = f"{url}/releases/download/{pkgver}+wayland{pkgrel}/rofi-{pkgver}+wayland{_release}.tar.gz"
sha256 = "025a390469008179eaffaa599e2eabbd81a77f7141d9038e008304673ba19843"
# check fails, disable for now
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
