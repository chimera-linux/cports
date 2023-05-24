pkgname = "atkmm"
pkgver = "2.36.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "at-spi2-core-devel",
    "glibmm-devel",
    "libsigc++-devel",
]
pkgdesc = "C++ accessibility interface bindings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6f62dd99f746985e573605937577ccfc944368f606a71ca46342d70e1cdae079"


@subpackage("atkmm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/atkmm-2.36",
        ]
    )
