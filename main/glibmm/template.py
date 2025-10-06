pkgname = "glibmm"
pkgver = "2.86.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "39c0e9f6da046d679390774efdb9ad564436236736dc2f7825e614b2d4087826"


@subpackage("glibmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.68",
            "usr/lib/giomm-2.68",
        ]
    )
