pkgname = "gtkmm"
pkgver = "4.20.0"
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
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/gtkmm/{pkgver[:-2]}/gtkmm-{pkgver}.tar.xz"
sha256 = "daad9bf9b70f90975f91781fc7a656c923a91374261f576c883cd3aebd59c833"


@subpackage("gtkmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-4.0",
        ]
    )
