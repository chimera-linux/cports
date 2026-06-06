pkgname = "sushi"
pkgver = "50.0"
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
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/sushi/{pkgver[:-2]}/sushi-{pkgver}.tar.xz"
sha256 = "ab25177908d5ccc58568769a81eb9b4f32306786e6c73618193ebf61a127ee00"
# gir
options = ["!cross"]
