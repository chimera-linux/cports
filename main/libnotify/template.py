pkgname = "libnotify"
pkgver = "0.8.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Ddocbook_docs=disabled",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "libxslt-progs",
    "docbook-xsl-nons",
    "gobject-introspection",
]
makedepends = [
    "glib-devel",
    "libpng-devel",
    "gdk-pixbuf-devel",
    "gtk+3-devel",
]
pkgdesc = "Desktop notification library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnotify"
source = f"$(GNOME_SITE)/libnotify/{pkgver[:-2]}/libnotify-{pkgver}.tar.xz"
sha256 = "8fa04d4ebdc155b0a239df88bd9f09e8f2739d5707a1390b427ab4985f83d25a"


@subpackage("libnotify-devel")
def _(self):
    return self.default_devel()
