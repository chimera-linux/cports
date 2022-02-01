pkgname = "glibmm"
pkgver = "2.70.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "glib-devel", "perl", "pkgconf"]
makedepends = ["libglib-devel", "libsigc++-devel"]
checkdepends = ["glib-networking"]
pkgdesc = "C++ bindings for GLib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8008fd8aeddcc867a3f97f113de625f6e96ef98cf7860379813a9c0feffdb520"

@subpackage("glibmm-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/glibmm-2.68",
        "usr/lib/giomm-2.68",
    ])
