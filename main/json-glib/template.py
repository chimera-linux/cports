pkgname = "json-glib"
pkgver = "1.10.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dinstalled_tests=false"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel"]
pkgdesc = "JSON parser for glib-based projects"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/action/show/Projects/JsonGlib"
source = f"$(GNOME_SITE)/json-glib/{pkgver[:-2]}/json-glib-{pkgver}.tar.xz"
sha256 = "77f4bcbf9339528f166b8073458693f0a20b77b7059dbc2db61746a1928b0293"


@subpackage("json-glib-devel")
def _(self):
    return self.default_devel()
