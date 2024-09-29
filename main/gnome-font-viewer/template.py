pkgname = "gnome-font-viewer"
pkgver = "47.0"
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
source = f"$(GNOME_SITE)/gnome-font-viewer/{pkgver[:-2]}/gnome-font-viewer-{pkgver}.tar.xz"
sha256 = "b8e5a042e0b241b0c7cae43f74da0d5f88e6423017a91feb86e7617edb4080ed"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
