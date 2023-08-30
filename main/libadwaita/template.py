pkgname = "libadwaita"
pkgver = "1.3.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala-devel",
    "gettext",
    "sassc",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "harfbuzz-devel",
]
checkdepends = ["weston", "fonts-cantarell-otf"]
pkgdesc = "GTK4 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libadwaita"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "801ccaf3a760213b59ebb9b8185327df225049544aee68a1340b165710acb1bd"
options = ["!cross"]


@subpackage("libadwaita-devel")
def _devel(self):
    return self.default_devel()
