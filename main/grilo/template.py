pkgname = "grilo"
pkgver = "0.3.15"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-introspection=true", "-Denable-vala=true",
    "-Denable-gtk-doc=false", "-Dsoup3=true",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "gettext-tiny", "vala",
]
makedepends = [
    "glib-devel", "libxml2-devel", "libsoup-devel", "gtk+3-devel",
    "liboauth-devel", "totem-pl-parser-devel",
]
pkgdesc = "Framework for media discovery"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Grilo"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f352acf73665669934270636fede66b52da6801fe20f638c4048ab2678577b2d"

@subpackage("grilo-devel")
def _devel(self):
    return self.default_devel()
