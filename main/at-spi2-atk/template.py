pkgname = "at-spi2-atk"
pkgver = "2.38.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny",
]
makedepends = [
    "libglib-devel", "atk-devel", "at-spi2-core-devel", "libxml2-devel"
]
pkgdesc = "GTK+ module that bridges ATK to D-Bus AT-SPI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/at-spi2-atk"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cfa008a5af822b36ae6287f18182c40c91dd699c55faa38605881ed175ca464f"
# non-trivial dbus setup
options = ["!check"]

@subpackage("at-spi2-atk-devel")
def _devel(self):
    return self.default_devel()
