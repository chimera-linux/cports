pkgname = "atk"
pkgver = "2.36.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "gobject-introspection",
]
makedepends = [
    "libglib-devel",
]
pkgdesc = "Interfaces for accessibility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/atk"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fb76247e369402be23f1f5c65d38a9639c1164d934e40f6a9cf3c9e96b652788"

@subpackage("atk-static")
def _static(self):
    return self.default_static()

@subpackage("atk-devel")
def _devel(self):
    return self.default_devel()
