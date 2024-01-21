pkgname = "libjcat"
pkgver = "0.2.1"
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
sha256 = "f623815ac855471277dc9d1b3b5ada1a9aaad6da67659c751dc3dec899dc2658"
options = ["!cross"]


@subpackage("libjcat-devel")
def _devel(self):
    return self.default_devel()
