pkgname = "mangowm-wlonly"
pkgver = "0.18.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "cjson-devel",
    "hwdata-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libinput-devel",
    "libliftoff-devel",
    "libseat-seatd",
    "libxcb-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "pcre2-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["xwayland"]
pkgdesc = "Fast and feature-rich Wayland compositor"
subdesc = "wl-only"
license = "GPL-3.0-or-later"
url = "https://mangowm.github.io"
source = "https://github.com/mangowm/mango/archive/d878ec0.tar.gz"
sha256 = "f2ba5a15fdf0691790cd098349aa981c3e152c449d82dbc42ffa3b351958bb48"
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
