pkgname = "libadwaita"
pkgver = "1.2.3"
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
sha256 = "c2758122bc09eee02b612976365a4532b16d7ee482b75f57efc9a9de52161f05"
options = ["!cross"]

@subpackage("libadwaita-devel")
def _devel(self):
    return self.default_devel()
