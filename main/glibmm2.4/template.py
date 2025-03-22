pkgname = "glibmm2.4"
pkgver = "2.66.8"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++2-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib, API version 2.4"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "64f11d3b95a24e2a8d4166ecff518730f79ecc27222ef41faf7c7e0340fc9329"


@subpackage("glibmm2.4-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.4",
            "usr/lib/giomm-2.4",
        ]
    )
