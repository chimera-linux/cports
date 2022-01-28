pkgname = "gnome-font-viewer"
pkgver = "41.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny",
]
makedepends = [
    "gtk+3-devel", "libglib-devel", "libhandy-devel", "fontconfig-devel",
    "harfbuzz-devel", "freetype-devel", "gnome-desktop-devel",
]
pkgdesc = "Font viewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-font-viewer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5dd410331be070e4e034397f2754980e073851d50a2119f2fbf96adc6fe2e876"
