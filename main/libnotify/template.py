pkgname = "libnotify"
pkgver = "0.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled", "-Ddocbook_docs=disabled", "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xsltproc", "docbook-xsl",
    "gobject-introspection",
]
makedepends = [
    "glib-devel", "libpng-devel", "gdk-pixbuf-devel", "gtk+3-devel",
]
pkgdesc = "Desktop notification library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnotify"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c5f4ed3d1f86e5b118c76415aacb861873ed3e6f0c6b3181b828cf584fc5c616"

@subpackage("libnotify-devel")
def _devel(self):
    return self.default_devel()
