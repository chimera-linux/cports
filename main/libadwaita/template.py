pkgname = "libadwaita"
pkgver = "1.1.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false", "-Dtests=true", "-Dgtk_doc=false", "-Dvapi=true",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala-devel",
    "gettext-tiny", "sassc",
]
makedepends = [
    "gtk4-devel", "libglib-devel", "harfbuzz-devel",
]
checkdepends = ["xserver-xorg-xvfb", "fonts-cantarell-otf"]
pkgdesc = "GTK4 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libadwaita"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fcc6d56669d33ac3d030098d7571d8045a02e18dc083b49a5a5a6325068e6b58"
options = ["!cross"]

@subpackage("libadwaita-devel")
def _devel(self):
    return self.default_devel()
