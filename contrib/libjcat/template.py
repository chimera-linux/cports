pkgname = "libjcat"
pkgver = "0.1.14"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gnutls-progs",
    "gobject-introspection",
    "help2man",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gnutls-devel",
    "gpgme-devel",
    "json-glib-devel",
]
pkgdesc = "Library for Jcat file manipulation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libjcat"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "e754051419d9955cfa4dcf4503aa86105c45bcbb5e95222a938ba95cc8f0569b"
options=  ["!cross"]


@subpackage("libjcat-devel")
def _devel(self):
    return self.default_devel()
