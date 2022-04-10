pkgname = "gnome-font-viewer"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "libglib-devel", "fontconfig-devel",
    "harfbuzz-devel", "freetype-devel", "gnome-desktop-devel",
]
pkgdesc = "Font viewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-font-viewer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cfa2b8dfff21a105a1a021dadfa213f13627e6a179a77c7b59fdcedaca848dcc"
