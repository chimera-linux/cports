pkgname = "gtksourceview4"
pkgver = "4.8.4"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dglade_catalog=false",
    "-Dgir=true",
    "-Dvapi=true",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-devel",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libxml2-devel",
    "vala",
]
pkgdesc = "Advanced Gtk+ text editor widget"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GtkSourceView"
source = (
    f"$(GNOME_SITE)/gtksourceview/{pkgver[:-2]}/gtksourceview-{pkgver}.tar.xz"
)
sha256 = "7ec9d18fb283d1f84a3a3eff3b7a72b09a10c9c006597b3fbabbb5958420a87d"
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("gtksourceview4-devel")
def _(self):
    return self.default_devel()
