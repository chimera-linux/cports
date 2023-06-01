pkgname = "sushi"
pkgver = "44.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "gettext-tiny",
    "gjs",
]
makedepends = [
    "glib-devel",
    "libepoxy-devel",
    "freetype-devel",
    "evince-devel",
    "gdk-pixbuf-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "harfbuzz-devel",
    "webkitgtk-devel",
]
depends = ["evince", "nautilus"]
pkgdesc = "File previewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6c002fe0aea19027ba448b5aec94d5cd753c9752f996ee033152428738ea43e9"
