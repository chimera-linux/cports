pkgname = "gtkmm"
pkgver = "4.14.0"
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
sha256 = "9350a0444b744ca3dc69586ebd1b6707520922b6d9f4f232103ce603a271ecda"


@subpackage("gtkmm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-4.0",
        ]
    )
