pkgname = "gtksourceview4"
pkgver = "4.8.2"
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
sha256 = "842de7e5cb52000fd810e4be39cd9fe29ffa87477f15da85c18f7b82d45637cc"
# needs graphical environment
options = ["!check"]

@subpackage("gtksourceview4-devel")
def _devel(self):
    return self.default_devel()
