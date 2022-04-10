pkgname = "gtksourceview4"
pkgver = "4.8.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dglade_catalog=true", "-Dgir=true", "-Dvapi=true", "-Dgtk_doc=false"
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "vala", "glib-devel",
    "gtk+3-devel", "gettext-tiny", "xsltproc"
]
makedepends = [
    "glade3-devel", "gtk+3-devel", "libglib-devel", "libxml2-devel", "vala"
]
pkgdesc = "Advanced Gtk+ text editor widget"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GtkSourceView"
source = f"$(GNOME_SITE)/gtksourceview/{pkgver[:-2]}/gtksourceview-{pkgver}.tar.xz"
sha256 = "c30019506320ca2474d834cced1e2217ea533e00eb2a3f4eb7879007940ec682"
# needs graphical environment
options = ["!check", "!cross"]

@subpackage("gtksourceview4-devel")
def _devel(self):
    return self.default_devel()
