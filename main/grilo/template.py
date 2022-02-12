pkgname = "grilo"
pkgver = "0.3.14"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-introspection=true", "-Denable-vala=true",
    "-Denable-gtk-doc=false",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "gettext-tiny", "vala",
]
makedepends = [
    "libglib-devel", "libxml2-devel", "libsoup-devel", "gtk+3-devel",
    "liboauth-devel", "totem-pl-parser-devel",
]
pkgdesc = "Framework for media discovery"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Grilo"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0369d0b00bb0f59ba5f7aea8cfc665f38df14a5b4182d28c7c1e2cd15b518743"

@subpackage("grilo-devel")
def _devel(self):
    return self.default_devel()
