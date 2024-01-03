pkgname = "libjcat"
pkgver = "0.2.0"
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
sha256 = "14d5b35c557c893de30dc7631e07bb981a6aebb3611ac245c862a4af0f0371b6"
options = ["!cross"]


@subpackage("libjcat-devel")
def _devel(self):
    return self.default_devel()
