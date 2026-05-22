pkgname = "awesome"
pkgver = "4.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DSYSCONFDIR=/etc",
]
hostmakedepends = [
    "asciidoctor",
    "clang",
    "cmake",
    "imagemagick",
    "lua5.4",
    "lua5.4-lgi",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "libxcb-devel",
    "libxdg-basedir-devel",
    "libxkbcommon-devel",
    "lua5.4-devel",
    "lua5.4-lgi",
    "pango-devel",
    "startup-notification-devel",
    "xcb-util-cursor-devel",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
    "xcb-util-xrm-devel",
    "xorgproto",
]
depends = [
    "dbus",
    "lua5.4-lgi",
    "pango",
]
pkgdesc = "Highly configurable, next gen framework window manager for X"
license = "GPL-2.0-or-later"
url = "https://awesomewm.org"
source = f"https://github.com/awesomeWM/awesome/releases/download/v{pkgver}/awesome-{pkgver}.tar.xz"
sha256 = "78264d6f012350b371e339127aca485260bc0aa935eff578ba75ce1a00e11753"
tool_flags = {"CFLAGS": ["-fcommon"]}
env = {"AWESOME_IGNORE_LGI": "1"}


def post_install(self):
    self.install_license("LICENSE")
