pkgname = "awesome"
pkgver = "4.3"
pkgrel = 0
build_style = "cmake"
_luaver = "5.4"
configure_args = [
    "-DSYSCONFDIR=/etc",
]
hostmakedepends = [
    "asciidoctor",
    "cmake",
    "imagemagick",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxdg-basedir-devel",
    "libxkbcommon-devel",
    "startup-notification-devel",
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
    "xcb-util-xrm-devel",
    f"lua{_luaver}-devel",
    f"lua{_luaver}-lgi",
]
depends = [
    f"lua{_luaver}",
    f"lua{_luaver}-lgi",
]
pkgdesc = "Highly configurable, next generation framework window manager"
maintainer = "dlatchx <dlatchx@tfnux.org>"
license = "GPL-2.0-or-later"
url = "https://awesomewm.org"
source = (
    f"https://github.com/awesomeWM/awesome/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b8a509464fb964acfc0cfaa4c689beaceb0f720de3983053d54d440158c281dd"
tool_flags = {
    "CFLAGS": ["-fcommon"],
}
hardening = ["vis"]
