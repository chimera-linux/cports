pkgname = "gnome-font-viewer"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
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
sha256 = "9564b088c5b150c54e2a3a7bc7014deec6ee551261e98488f891b1f1b8dc6b80"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
