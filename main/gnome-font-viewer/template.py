pkgname = "gnome-font-viewer"
pkgver = "47_alpha"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "glib-devel",
    "fontconfig-devel",
    "harfbuzz-devel",
    "freetype-devel",
    "gnome-desktop-devel",
]
pkgdesc = "Font viewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-font-viewer"
source = f"$(GNOME_SITE)/gnome-font-viewer/{pkgver[:2]}/gnome-font-viewer-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "5305c5ef54d742a3d641443ab5513e2c98f915e2fb0afc7c5f326d200a461f2f"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
