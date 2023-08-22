pkgname = "totem-pl-parser"
pkgver = "3.26.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-libarchive=yes",
    "-Denable-libgcrypt=yes",
    "-Denable-uchardet=yes",
    "-Dintrospection=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext",
]
makedepends = [
    "glib-devel",
    "libxml2-devel",
    "uchardet-devel",
    "libgcrypt-devel",
    "libarchive-devel",
]
pkgdesc = "Totem playlist parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/totem-pl-parser"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c0df0f68d5cf9d7da43c81c7f13f11158358368f98c22d47722f3bd04bd3ac1c"
# needs network access
options = ["!check"]


@subpackage("totem-pl-parser-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libtotem-plparser-mini")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (totem-plparser-mini library)"

    return ["usr/lib/libtotem-plparser-mini.so.*"]
