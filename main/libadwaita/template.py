pkgname = "libadwaita"
pkgver = "1.3.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala-devel",
    "gettext-tiny",
    "sassc",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "harfbuzz-devel",
]
checkdepends = ["xserver-xorg-xvfb", "fonts-cantarell-otf"]
pkgdesc = "GTK4 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libadwaita"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b38c91658b2d1fcb7eedf687858b0a54de39af6357661912b54271884c8e195e"
options = ["!cross"]


@subpackage("libadwaita-devel")
def _devel(self):
    return self.default_devel()
