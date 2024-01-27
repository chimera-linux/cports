pkgname = "pangomm"
pkgver = "2.50.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm-devel", "cairomm-devel"]
pkgdesc = "C++ bindings for Pango"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1bc5ab4ea3280442580d68318226dab36ceedfc3288f9d83711cf7cfab50a9fb"


@subpackage("pangomm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/pangomm-2.48",
        ]
    )
