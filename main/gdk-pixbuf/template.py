pkgname = "gdk-pixbuf"
pkgver = "2.42.8"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled", "-Dinstalled_tests=false",
]
hostmakedepends = [
    "meson", "gettext-tiny", "pkgconf", "docbook-xsl-nons", "xsltproc",
    "glib-devel", "gobject-introspection",
]
makedepends = [
    "libglib-devel", "libpng-devel", "libtiff-devel", "shared-mime-info",
]
depends = ["shared-mime-info"]
triggers = ["/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders"]
pkgdesc = "Image loading library for GTK"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GdkPixbuf"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "84acea3acb2411b29134b32015a5b1aaa62844b19c4b1ef8b8971c6b0759f4c6"

@subpackage("gdk-pixbuf-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/bin/*csource*",
        "usr/share/man/man1/*csource*",
    ])
