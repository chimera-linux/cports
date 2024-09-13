pkgname = "gtkmm"
pkgver = "4.16.0"
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
sha256 = "3b23fd3abf8fb223b00e9983b6010af2db80e38c89ab6994b8b6230aa85d60f9"


@subpackage("gtkmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-4.0",
        ]
    )
