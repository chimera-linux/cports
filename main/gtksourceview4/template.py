pkgname = "gtksourceview4"
pkgver = "4.8.4"
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
    "glade3-devel", "gtk+3-devel", "glib-devel", "libxml2-devel", "vala"
]
pkgdesc = "Advanced Gtk+ text editor widget"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GtkSourceView"
source = f"$(GNOME_SITE)/gtksourceview/{pkgver[:-2]}/gtksourceview-{pkgver}.tar.xz"
sha256 = "7ec9d18fb283d1f84a3a3eff3b7a72b09a10c9c006597b3fbabbb5958420a87d"
# needs graphical environment
options = ["!check", "!cross"]

@subpackage("gtksourceview4-devel")
def _devel(self):
    return self.default_devel()
