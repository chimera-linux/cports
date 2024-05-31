pkgname = "gtksourceview"
pkgver = "5.12.1"
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
sha256 = "84c82aad985c5aadae7cea7804904a76341ec82b268d46594c1a478f39b42c1f"
# needs graphical environment
# lto results in broken mouse scrolling in gnome-text-editor
options = ["!check", "!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _devel(self):
    return self.default_devel()
