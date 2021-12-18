pkgname = "gdk-pixbuf"
pkgver = "2.42.6"
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
pkgdesc = "Image loading library for GTK"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GdkPixbuf"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c4a6b75b7ed8f58ca48da830b9fa00ed96d668d3ab4b1f723dcf902f78bde77f"

@subpackage("gdk-pixbuf-static")
def _static(self):
    return self.default_static()

@subpackage("gdk-pixbuf-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/bin/*csource*",
        "usr/share/man/man1/*csource*",
    ])
