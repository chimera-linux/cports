pkgname = "json-glib"
pkgver = "1.6.6"
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
sha256 = "96ec98be7a91f6dde33636720e3da2ff6ecbb90e76ccaa49497f31a6855a490e"

@subpackage("json-glib-devel")
def _devel(self):
    return self.default_devel()
