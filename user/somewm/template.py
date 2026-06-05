pkgname = "somewm"
pkgver = "1.4.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-devel",
    "wayland-protocols",
]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "gdk-pixbuf-devel",
    "libdrm-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "lua5.1-lgi",
    "luajit-devel",
    "pango-devel",
    "wlroots0.19-devel",
    "xcb-util-devel",
]
pkgdesc = "Not quite awesome... just some. - AwesomeWM fork which uses Wayland"
license = "GPL-3.0-only"
url = "https://somewm.org"
source = (
    f"https://github.com/trip-zip/somewm/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "a9cec46c38184b5141bc7bc6f72838f3ae0428bcaec7ee558839f08e518d0369"
