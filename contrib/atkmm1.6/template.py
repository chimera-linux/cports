pkgname = "atkmm1.6"
pkgver = "2.28.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "at-spi2-core-devel",
    "glibmm2.4-devel",
    "libsigc++2-devel",
]
pkgdesc = "C++ accessibility interface bindings (2.28)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/atkmm/{pkgver[:-2]}/atkmm-{pkgver}.tar.xz"
sha256 = "0a142a8128f83c001efb8014ee463e9a766054ef84686af953135e04d28fdab3"


@subpackage("atkmm1.6-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/atkmm-1.6",
        ]
    )
