pkgname = "gnome-font-viewer"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gtk4-devel",
    "harfbuzz-devel",
    "libadwaita-devel",
]
pkgdesc = "Font viewer for GNOME"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-font-viewer"
source = f"$(GNOME_SITE)/gnome-font-viewer/{pkgver[:-2]}/gnome-font-viewer-{pkgver}.tar.xz"
sha256 = "732624231b624ff5c7ac03a8ce71be12393daa53551d11550b20d7b0a3a872a7"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
