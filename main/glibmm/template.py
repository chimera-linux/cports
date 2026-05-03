pkgname = "glibmm"
pkgver = "2.88.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "a6549da3a6c43de83b8717dae5413c57a60d92f6ecc624615c612d0bb0ad0fe2"


@subpackage("glibmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.68",
            "usr/lib/giomm-2.68",
        ]
    )
