pkgname = "mangowl"
pkgver = "0.18.5"
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
source = "https://github.com/mangowm/mango/archive/26e3708.tar.gz"
sha256 = "94757f760b7225ffce2d3274e679623dd52d1c77c2cae5cca6c33637cc584f15"
hardening = ["vis", "cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
