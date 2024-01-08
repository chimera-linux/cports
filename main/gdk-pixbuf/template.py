pkgname = "gdk-pixbuf"
pkgver = "2.42.10"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dinstalled_tests=false",
]
hostmakedepends = [
    "meson",
    "gettext",
    "pkgconf",
    "docbook-xsl-nons",
    "xsltproc",
    "glib-devel",
    "gobject-introspection",
    "python-docutils",
]
makedepends = [
    "glib-devel",
    "libpng-devel",
    "libtiff-devel",
    "shared-mime-info",
]
depends = ["shared-mime-info"]
triggers = ["/usr/lib/gdk-pixbuf-2.0/2.10.0/loaders"]
pkgdesc = "Image loading library for GTK"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GdkPixbuf"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ee9b6c75d13ba096907a2e3c6b27b61bcd17f5c7ebeab5a5b439d2f2e39fe44b"
# FIXME int
hardening = ["!int"]
# pixbuf-randomly-modified aborts, FIXME
options = ["!check"]


@subpackage("gdk-pixbuf-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/bin/*csource*",
            "usr/share/man/man1/*csource*",
        ]
    )
