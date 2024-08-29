pkgname = "glibmm"
pkgver = "2.82.0"
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
sha256 = "38684cff317273615c67b8fa9806f16299d51e5506d9b909bae15b589fa99cb6"


@subpackage("glibmm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/glibmm-2.68",
            "usr/lib/giomm-2.68",
        ]
    )
