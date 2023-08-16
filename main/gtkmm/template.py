pkgname = "gtkmm"
pkgver = "4.12.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["xvfb-run"]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "gtk4-devel",
    "cairomm-devel",
    "pangomm-devel",
    "gdk-pixbuf-devel",
    "libepoxy-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "C++ bindings for Gtk4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/gtkmm/{pkgver[:-2]}/gtkmm-{pkgver}.tar.xz"
sha256 = "fbc3e7618123345c0148ef71abb6548d421f52bb224fbda34875b677dc032c92"


@subpackage("gtkmm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-4.0",
        ]
    )
