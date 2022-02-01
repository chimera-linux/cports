pkgname = "atkmm"
pkgver = "2.36.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["atk-devel", "glibmm-devel"]
pkgdesc = "C++ bindings for accessibility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.gtkmm.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e11324bfed1b6e330a02db25cecc145dca03fb0dff47f0710c85e317687da458"

@subpackage("atkmm-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/atkmm-2.36",
    ])
