pkgname = "libhandy"
pkgver = "1.5.0"
pkgrel = 0
build_style = "meson"
# TODO: glade
configure_args = [
    "-Dexamples=false", "-Dtests=false", "-Dgtk_doc=false", "-Dvapi=true",
    "-Dglade_catalog=disabled", "-Dintrospection=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala",
]
makedepends = [
    "gtk+3-devel", "libglib-devel"
]
pkgdesc = "GTK+3 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libhandy"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "466b9e026c1f9eb3b65966f530d97703a8212daaf911748c145e9cb843dbd6fe"
# needs x11
options = ["!check"]

@subpackage("libhandy-devel")
def _devel(self):
    return self.default_devel()
