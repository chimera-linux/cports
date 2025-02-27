pkgname = "libjcat"
pkgver = "0.2.3"
pkgrel = 0
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
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libjcat"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9b94aa1915ff392c466c03aa3ad8de320eb625d7a074571de9ec669ab17d405a"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/installed-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("libjcat-devel")
def _(self):
    return self.default_devel()
