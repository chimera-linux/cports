pkgname = "libnotify"
pkgver = "0.7.9"
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
    "libglib-devel", "libpng-devel", "gdk-pixbuf-devel", "gtk+3-devel",
]
pkgdesc = "Desktop notification library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnotify"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "66c0517ed16df7af258e83208faaf5069727dfd66995c4bbc51c16954d674761"

@subpackage("libnotify-devel")
def _devel(self):
    return self.default_devel()
