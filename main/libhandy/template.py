pkgname = "libhandy"
pkgver = "1.8.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dglade_catalog=disabled",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxml2-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "GTK+3 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libhandy"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "05b497229073ff557f10b326e074c5066f8743a302d4820ab97bcb5cd2dab087"
# gdk_seat_get_keyboard: assertion 'GDK_IS_SEAT (seat)' failed
options = ["!check"]


@subpackage("libhandy-devel")
def _devel(self):
    return self.default_devel()
