pkgname = "libhandy"
pkgver = "1.8.0"
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
sha256 = "6c2542c0578924b0c29b7ae6cb44eb26df38eb01d6d5ef3d7d0b0825763230e8"
# needs x11
options = ["!check"]

@subpackage("libhandy-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
