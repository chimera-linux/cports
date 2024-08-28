pkgname = "glibmm"
pkgver = "2.80.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "f1a0c0ec514e3774bf993396f17f72106b40912c7d7cc9d10da31ba15517e3f5"


@subpackage("glibmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.68",
            "usr/lib/giomm-2.68",
        ]
    )
