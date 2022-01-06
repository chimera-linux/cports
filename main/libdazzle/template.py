pkgname = "libdazzle"
pkgver = "3.42.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable_gtk_doc=false", "-Dwith_vapi=true", "-Dwith_introspection=true",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala",
]
makedepends = [
    "gtk+3-devel", "libglib-devel"
]
pkgdesc = "Library to delight your users with fancy features"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libdazzle"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "eae67a3b3d9cce408ee9ec0ab6adecb83e52eb53f9bc93713f4df1e84da16925"
# needs x11
options = ["!check"]

@subpackage("libdazzle-devel")
def _devel(self):
    return self.default_devel()
