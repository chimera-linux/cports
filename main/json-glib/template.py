pkgname = "json-glib"
pkgver = "1.10.0"
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
sha256 = "1bca8d66d96106ecc147df3133b95a5bb784f1fa6f15d06dd7c1a8fb4a10af7b"


@subpackage("json-glib-devel")
def _(self):
    return self.default_devel()
