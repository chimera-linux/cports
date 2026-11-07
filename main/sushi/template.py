pkgname = "sushi"
pkgver = "51.2"
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
depends = ["gtksourceview4", "nautilus", "papers", "webkitgtk"]
pkgdesc = "File previewer for GNOME"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/sushi/{pkgver[:-2]}/sushi-{pkgver}.tar.xz"
sha256 = "928c0155bd5664098bdb4d591806e70e8219a4b66bf46c95382f72589e4e9a6e"
# gir
options = ["!cross"]
