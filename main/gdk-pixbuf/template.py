pkgname = "gdk-pixbuf"
pkgver = "2.42.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled", "-Dinstalled_tests=false",
]
hostmakedepends = [
    "meson", "gettext-tiny", "pkgconf", "docbook-xsl-nons", "xsltproc",
    "glib-devel", "gobject-introspection", "python-docutils",
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
sha256 = "28f7958e7bf29a32d4e963556d241d0a41a6786582ff6a5ad11665e0347fc962"

@subpackage("gdk-pixbuf-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/bin/*csource*",
        "usr/share/man/man1/*csource*",
    ])
