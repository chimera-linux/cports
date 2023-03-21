pkgname = "glibmm"
pkgver = "2.76.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8637d80ceabd94fddd6e48970a082a264558d4ab82684e15ffc87e7ef3462ab2"

@subpackage("glibmm-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/glibmm-2.68",
        "usr/lib/giomm-2.68",
    ])
