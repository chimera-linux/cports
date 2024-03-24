pkgname = "pangomm"
pkgver = "2.52.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm-devel", "cairomm-devel"]
pkgdesc = "C++ bindings for Pango"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "34a134126a6484ff12f774358c36ecc44d0e9df094e1b83796d9774bb7d24947"


@subpackage("pangomm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/pangomm-2.48",
        ]
    )
