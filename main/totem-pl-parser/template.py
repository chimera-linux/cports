pkgname = "totem-pl-parser"
pkgver = "3.26.6"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Denable-libarchive=yes",
    "-Denable-libgcrypt=yes",
    "-Denable-uchardet=yes",
    "-Dintrospection=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "libarchive-devel",
    "libgcrypt-devel",
    "libxml2-devel",
    "uchardet-devel",
]
# transitional
provides = [self.with_pkgver("libtotem-plparser-mini")]
pkgdesc = "Totem playlist parser library"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/totem-pl-parser"
source = f"$(GNOME_SITE)/totem-pl-parser/{pkgver[:-2]}/totem-pl-parser-{pkgver}.tar.xz"
sha256 = "c0df0f68d5cf9d7da43c81c7f13f11158358368f98c22d47722f3bd04bd3ac1c"
# needs network access
options = ["!check", "linkundefver"]


@subpackage("totem-pl-parser-devel")
def _(self):
    return self.default_devel()
