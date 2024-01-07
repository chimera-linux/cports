pkgname = "gtkmm3.0"
pkgver = "3.24.8"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dbuild-demos=false", "-Dbuild-tests=true"]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = [
    "gtk+3-devel",
    "cairomm1.0-devel",
    "pangomm1.4-devel",
    "atkmm1.6-devel",
    "gdk-pixbuf-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "C++ bindings for Gtk+3"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/gtkmm/{pkgver[:-2]}/gtkmm-{pkgver}.tar.xz"
sha256 = "d2940c64922e5b958554b23d4c41d1839ea9e43e0d2e5b3819cfb46824a098c4"


@subpackage("gtkmm3.0-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-3.0",
        ]
    )
