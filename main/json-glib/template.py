pkgname = "json-glib"
pkgver = "1.8.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gobject-introspection"]
makedepends = ["glib-devel"]
pkgdesc = "JSON parser for glib-based projects"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/action/show/Projects/JsonGlib"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "97ef5eb92ca811039ad50a65f06633f1aae64792789307be7170795d8b319454"


@subpackage("json-glib-devel")
def _devel(self):
    return self.default_devel()
