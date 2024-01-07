pkgname = "gtksourceview"
pkgver = "5.10.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dvapi=true", "-Dgtk_doc=false"]
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
sha256 = "b38a3010c34f59e13b05175e9d20ca02a3110443fec2b1e5747413801bc9c23f"
# needs graphical environment
# lto results in broken mouse scrolling in gnome-text-editor
options = ["!check", "!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _devel(self):
    return self.default_devel()
