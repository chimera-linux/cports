pkgname = "totem-pl-parser"
pkgver = "3.26.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
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
sha256 = "60d517c1acabe54ae337f64451264fc76730696eaae26b5480fb37166689b5f3"
# needs network access
options = ["!check", "linkundefver"]


@subpackage("totem-pl-parser-devel")
def _(self):
    return self.default_devel()
