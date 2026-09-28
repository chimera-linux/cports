pkgname = "glibmm2.4"
pkgver = "2.66.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++2-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib, API version 2.4"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-3]}/glibmm-{pkgver}.tar.xz"
sha256 = "2b61780203aed98e701d3ea57c8f353e7c8ada9706a79be782f6c5153dd035c0"


@subpackage("glibmm2.4-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.4",
            "usr/lib/giomm-2.4",
        ]
    )
