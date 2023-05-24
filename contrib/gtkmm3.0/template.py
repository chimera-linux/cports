pkgname = "gtkmm3.0"
pkgver = "3.24.7"
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
sha256 = "1d7a35af9c5ceccacb244ee3c2deb9b245720d8510ac5c7e6f4b6f9947e6789c"


@subpackage("gtkmm3.0-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/gtkmm-3.0",
        ]
    )
