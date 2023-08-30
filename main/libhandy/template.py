pkgname = "libhandy"
pkgver = "1.8.2"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dexamples=false",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dglade_catalog=disabled",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
    "libxml2-progs",
    "gettext",
]
makedepends = [
    "gtk+3-devel",
    "glib-devel",
]
checkdepends = ["weston"]
pkgdesc = "GTK+3 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libhandy"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d11aa2cd3e570ac6d0efdba46d173147c11f45826457e924c05990bb2e0df9ad"
# gdk_seat_get_keyboard: assertion 'GDK_IS_SEAT (seat)' failed
options = ["!check"]


@subpackage("libhandy-devel")
def _devel(self):
    return self.default_devel()
