pkgname = "libhandy"
pkgver = "1.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dglade_catalog=enabled",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
    "libxml2-progs",
    "gettext-tiny",
]
makedepends = [
    "gtk+3-devel",
    "glib-devel",
    "glade3-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "GTK+3 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libhandy"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d11aa2cd3e570ac6d0efdba46d173147c11f45826457e924c05990bb2e0df9ad"


@subpackage("libhandy-devel")
def _devel(self):
    return self.default_devel()
