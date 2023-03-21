pkgname = "sushi"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection",
    "gettext-tiny", "gjs"
]
makedepends = [
    "glib-devel", "libepoxy-devel", "freetype-devel", "evince-devel",
    "gdk-pixbuf-devel", "gstreamer-devel", "gst-plugins-base-devel",
    "gtk+3-devel", "gtksourceview4-devel", "harfbuzz-devel", "webkitgtk-devel",
]
depends = ["evince", "nautilus"]
pkgdesc = "File previewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/sushi"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "57848526149ab1c784fb92fbc934c3514fe522aba649d5d9fedec7e1b147527b"
