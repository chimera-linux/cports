pkgname = "gexiv2"
pkgver = "0.14.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Dvapi=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "python-gobject",
    "vala",
]
makedepends = ["glib-devel", "exiv2-devel"]
pkgdesc = "GObject wrapper for exiv2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gexiv2"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ec3ee3ec3860b9c78958a55da89cf76ae2305848e12f41945b7b52124d8f6cf9"


@subpackage("gexiv2-devel")
def _devel(self):
    return self.default_devel()
