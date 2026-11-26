pkgname = "mango"
pkgver = "0.19.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "cjson-devel",
    "libdrm-devel",
    "libglvnd-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "pcre2-devel",
    "pixman-devel",
    "scenefx-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
    "xcb-util-wm-devel",
]
depends = ["xwayland"]
pkgdesc = "Lightweight and feature-rich Wayland compositor"
license = "GPL-3.0-or-later"
url = "https://github.com/mangowm/mango"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c4573ab52e76d38850d2b5e6982fcf16ee1f664cb327bd88a5b05f26676642fa"
options = ["etcfiles"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
