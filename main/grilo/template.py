pkgname = "grilo"
pkgver = "0.3.16"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-introspection=true",
    "-Denable-vala=true",
    "-Denable-gtk-doc=false",
    "-Dsoup3=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext-tiny",
    "vala",
]
makedepends = [
    "glib-devel",
    "libxml2-devel",
    "libsoup-devel",
    "gtk+3-devel",
    "liboauth-devel",
    "totem-pl-parser-devel",
]
pkgdesc = "Framework for media discovery"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Grilo"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "884580e8c5ece280df23aa63ff5234b7d48988a404df7d6bfccd1e77b473bd96"


@subpackage("grilo-devel")
def _devel(self):
    return self.default_devel()
