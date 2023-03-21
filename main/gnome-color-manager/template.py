pkgname = "gnome-color-manager"
pkgver = "3.36.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext-tiny", "itstool"]
makedepends = [
    "glib-devel", "colord-devel", "lcms2-devel", "gtk+3-devel",
    "libcanberra-devel",
]
depends = ["colord", "shared-color-targets"]
pkgdesc = "Color profile manager for the GNOME desktop"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-color-manager"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "9ddb9e6b6472e119801381f90905332ec1d4258981721bba831ca246ceb3ad3b"
# FIXME cfi
hardening = ["vis", "!cfi"]
# needs a graphical environment
options = ["!check"]
