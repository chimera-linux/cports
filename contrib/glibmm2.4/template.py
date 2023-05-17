pkgname = "glibmm2.4"
pkgver = "2.66.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["glib-devel", "libsigc++2-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib (2.4)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/glibmm/{pkgver[:-2]}/glibmm-{pkgver}.tar.xz"
sha256 = "5358742598181e5351d7bf8da072bf93e6dd5f178d27640d4e462bc8f14e152f"

@subpackage("glibmm2.4-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/glibmm-2.4",
        "usr/lib/giomm-2.4",
    ])
