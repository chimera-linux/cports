pkgname = "grilo"
pkgver = "0.3.19"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-introspection=true",
    "-Denable-vala=true",
    "-Denable-gtk-doc=false",
    "-Dsoup3=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "liboauth-devel",
    "libsoup-devel",
    "libxml2-devel",
    "totem-pl-parser-devel",
]
pkgdesc = "Framework for media discovery"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Grilo"
source = f"$(GNOME_SITE)/grilo/{pkgver[:-3]}/grilo-{pkgver}.tar.xz"
sha256 = "0869c81d19ab139c667d79567c14ddcb6cb5cbfc0108d04cade287eb29536706"


@subpackage("grilo-devel")
def _(self):
    return self.default_devel()
