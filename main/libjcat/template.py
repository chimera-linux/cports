pkgname = "libjcat"
pkgver = "0.2.2"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
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
sha256 = "60fb1d30b16ba1a2dbf48998094d366bc94a082846b71decf9d6ac6bb6aa4800"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/installed-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("libjcat-devel")
def _(self):
    return self.default_devel()
