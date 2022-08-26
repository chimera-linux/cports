pkgname = "sushi"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection",
    "gettext-tiny", "gjs"
]
makedepends = [
    "libglib-devel", "libepoxy-devel", "freetype-devel", "evince-devel",
    "gdk-pixbuf-devel", "gstreamer-devel", "gst-plugins-base-devel",
    "gtk+3-devel", "gtksourceview4-devel", "harfbuzz-devel", "webkitgtk-devel",
]
depends = ["evince", "nautilus"]
pkgdesc = "File previewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "45d8db7af45a79784e7a34588d149ea955c8be44bb82a36e896829405b7c8820"
