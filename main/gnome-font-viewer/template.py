pkgname = "gnome-font-viewer"
pkgver = "49.0"
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
sha256 = "7c018925c285771b55d7d1a6f15711c0c193d7450ed9871e20d44f2548562404"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
