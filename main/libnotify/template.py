pkgname = "libnotify"
pkgver = "0.8.3"
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
    "docbook-xsl",
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
sha256 = "ee8f3ef946156ad3406fdf45feedbdcd932dbd211ab4f16f75eba4f36fb2f6c0"


@subpackage("libnotify-devel")
def _(self):
    return self.default_devel()
