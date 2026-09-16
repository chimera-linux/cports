pkgname = "glibmm"
pkgver = "2.90.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "e2efa45643f16b9fea2d6299f2f403d672eaeacddf0ff7f8094e1af9b0f5980b"


@subpackage("glibmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.68",
            "usr/lib/giomm-2.68",
        ]
    )
