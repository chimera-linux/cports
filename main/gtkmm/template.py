pkgname = "gtkmm"
pkgver = "4.6.1"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["xvfb-run"]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "gtk4-devel", "cairomm-devel", "pangomm-devel",
    "gdk-pixbuf-devel", "libepoxy-devel"
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "C++ bindings for Gtk4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/gtkmm/{pkgver[:-2]}/gtkmm-{pkgver}.tar.xz"
sha256 = "0d5efeca9ec64fdd530bb8226c6310ac99549b3dd9604d6e367639791af3d1e0"

@subpackage("gtkmm-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/gtkmm-4.0",
    ])
