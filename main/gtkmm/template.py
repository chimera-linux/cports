pkgname = "gtkmm"
pkgver = "4.4.0"
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
sha256 = "2eb464326096e6a40c82e9cd074164d8103fb5e07865679c0a649e4174700dda"

@subpackage("gtkmm-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/gtkmm-4.0",
    ])
