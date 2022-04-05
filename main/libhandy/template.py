pkgname = "libhandy"
pkgver = "1.6.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false", "-Dtests=false", "-Dgtk_doc=false", "-Dvapi=true",
    "-Dglade_catalog=enabled", "-Dintrospection=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala",
    "libxml2-progs", "gettext-tiny",
]
makedepends = [
    "gtk+3-devel", "libglib-devel", "glade3-devel",
]
pkgdesc = "GTK+3 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libhandy"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6eab0384404d56bd1b1fa059d9a081177778f6ae080ffc2120f28656ca7462a4"
# needs x11
options = ["!check"]

@subpackage("libhandy-devel")
def _devel(self):
    return self.default_devel()
