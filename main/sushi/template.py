pkgname = "sushi"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "gjs",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "evince-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "harfbuzz-devel",
    "libepoxy-devel",
    "webkitgtk-devel",
]
depends = ["evince", "gtksourceview4", "nautilus", "webkitgtk"]
pkgdesc = "File previewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "96085baaa430ab2142c606aab5c47e2fbb2fd3eb70a352137e65c59a58a0f2c6"
# gir
options = ["!cross"]
