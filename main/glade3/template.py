pkgname = "glade3"
pkgver = "3.38.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgtk_doc=true", "-Dman=true", "-Dintrospection=true"
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gtk-doc-tools", "gettext-tiny-devel",
    "gobject-introspection", "gjs-devel", "yelp-tools", "itstool",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "python-gobject-devel", "webkitgtk-devel",
    "gjs-devel", "libxml2-devel",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "Gtk+3 user interface designer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://glade.gnome.org"
source = f"$(GNOME_SITE)/glade/{pkgver[:-2]}/glade-{pkgver}.tar.xz"
sha256 = "98fc87647d88505c97dd2f30f2db2d3e9527515b3af11694787d62a8d28fbab7"
# needs a graphical environment
options = ["!check"]

@subpackage("libgladeui3")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"
    self.depends += ["python-gobject"]

    return self.default_libs(extra = [
        "usr/lib/girepository-1.0",
        "usr/lib/glade/modules",
        "usr/share/glade",
        "usr/share/locale",
    ])

@subpackage("glade3-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/gtk-doc"])
