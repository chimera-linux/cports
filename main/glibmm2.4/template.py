pkgname = "glibmm2.4"
pkgver = "2.66.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++2-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib, API version 2.4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "fe02c1e5f5825940d82b56b6ec31a12c06c05c1583cfe62f934d0763e1e542b3"


@subpackage("glibmm2.4-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.4",
            "usr/lib/giomm-2.4",
        ]
    )
