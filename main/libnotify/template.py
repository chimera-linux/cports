pkgname = "libnotify"
pkgver = "0.8.1"
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
sha256 = "d033e6d4d6ccbf46a436c31628a4b661b36dca1f5d4174fe0173e274f4e62557"

@subpackage("libnotify-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
