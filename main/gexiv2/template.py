pkgname = "gexiv2"
pkgver = "0.14.2"
pkgrel = 1
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
sha256 = "2a0c9cf48fbe8b3435008866ffd40b8eddb0667d2212b42396fdf688e93ce0be"


@subpackage("gexiv2-devel")
def _devel(self):
    return self.default_devel()
