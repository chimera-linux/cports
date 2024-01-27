pkgname = "sushi"
pkgver = "45.0"
pkgrel = 1
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
sha256 = "6a5f14b05a3471fe43853cc2b0e1ae5484d7f9f86f7ea376179829b9bf4ac1dd"
