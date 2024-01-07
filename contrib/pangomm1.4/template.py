pkgname = "pangomm1.4"
pkgver = "2.46.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["pango-devel", "glibmm2.4-devel", "cairomm1.0-devel"]
pkgdesc = "C++ bindings for Pango (2.46)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/pangomm/{pkgver[:-2]}/pangomm-{pkgver}.tar.xz"
sha256 = "410fe04d471a608f3f0273d3a17d840241d911ed0ff2c758a9859c66c6f24379"


@subpackage("pangomm1.4-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/pangomm-1.4",
        ]
    )
