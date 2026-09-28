pkgname = "sushi"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "gettext",
    "gjs",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "freetype-devel",
    "glib-devel",
    "glycin-gtk4-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "harfbuzz-devel",
    "libepoxy-devel",
    "papers-devel",
    "webkitgtk4-devel",
]
depends = ["evince", "gtksourceview4", "nautilus", "webkitgtk"]
pkgdesc = "File previewer for GNOME"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/sushi/{pkgver[:-2]}/sushi-{pkgver}.tar.xz"
sha256 = "d41b1b9e640fd949895bf0e871143249eb7baa38ed4ba666dbb2427fbbc9e9a5"
# gir
options = ["!cross"]
