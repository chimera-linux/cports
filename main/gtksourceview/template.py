pkgname = "gtksourceview"
pkgver = "5.8.0"
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
sha256 = "110dd4c20def21886fbf777298fe0ef8cc2ad6023b8f36c7424411a414818933"
# needs graphical environment
# lto results in broken mouse scrolling in gnome-text-editor
options = ["!check", "!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _devel(self):
    return self.default_devel()
