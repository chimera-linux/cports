pkgname = "gtkmm"
pkgver = "4.15.1"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "cairomm-devel",
    "gdk-pixbuf-devel",
    "gtk4-devel",
    "libepoxy-devel",
    "pangomm-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "C++ bindings for Gtk4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/gtkmm/{pkgver[:-2]}/gtkmm-{pkgver}.tar.xz"
sha256 = "1b3576c951c96796fa36efa379ad614e34d86f91c0f8b56f4443011e0b10d157"


@subpackage("gtkmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-4.0",
        ]
    )
