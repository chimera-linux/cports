pkgname = "libdazzle"
pkgver = "3.44.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable_gtk_doc=false",
    "-Dwith_vapi=true",
    "-Dwith_introspection=true",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["gtk+3-devel", "glib-devel"]
pkgdesc = "Library to delight your users with fancy features"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/libdazzle"
source = f"$(GNOME_SITE)/libdazzle/{pkgver[:-2]}/libdazzle-{pkgver}.tar.xz"
sha256 = "3cd3e45eb6e2680cb05d52e1e80dd8f9d59d4765212f0e28f78e6c1783d18eae"
# needs x11
options = ["!check", "!cross"]


@subpackage("libdazzle-devel")
def _devel(self):
    return self.default_devel()
