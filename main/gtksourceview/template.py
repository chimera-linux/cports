pkgname = "gtksourceview"
pkgver = "5.12.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dvapi=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
    "glib-devel",
    "pcre2-devel",
    "gettext",
    "xsltproc",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libxml2-devel",
    "vala",
    "pcre2-devel",
]
pkgdesc = "Advanced Gtk4 text editor widget"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GtkSourceView"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "daf32ff5d3150d6385917d3503a85b9e047ba158b2b03079314c9c00813fa01f"
# needs graphical environment
# lto results in broken mouse scrolling in gnome-text-editor
options = ["!check", "!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _devel(self):
    return self.default_devel()
