pkgname = "awesome"

pkgdesc = "Highly configurable, next generation framework window manager"
license = "GPL-2.0-or-later"
maintainer = "dlatchx <dlatchx@tfnux.org>"
url = "https://awesomewm.org"

pkgver = "4.3"
pkgrel = 0

source = f"https://github.com/awesomeWM/awesome/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b8a509464fb964acfc0cfaa4c689beaceb0f720de3983053d54d440158c281dd"

_luaver = "5.4"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "imagemagick",
]
makedepends = [
    f"lua{_luaver}-devel",
    f"lua{_luaver}-lgi",
    "libxcb-devel",
    "glib-devel",
    "gdk-pixbuf-devel",
    "cairo-devel",
    "libx11-devel",
    "xcb-util-devel",
    "xcb-util-cursor-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
    "libxkbcommon-devel",
    "startup-notification-devel",
    "libxdg-basedir-devel",
    "xcb-util-xrm-devel",
]
depends = [
    f"lua{_luaver}",
    f"lua{_luaver}-lgi",
]

build_style = "cmake"

tool_flags = {
    "CFLAGS": ["-fcommon"],
}

configure_args = [
    "-DCMAKE_BUILD_TYPE=RELEASE",
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DSYSCONFDIR=/etc",
]

hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")
