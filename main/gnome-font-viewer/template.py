pkgname = "gnome-font-viewer"
pkgver = "45.0"
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "97cb6b68dda60de0ab3038383586f1e4bc1da5a48f44025bd6bbe74ea05c2b08"
# FIXME cfi
hardening = ["vis", "!cfi"]

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
