pkgname = "colord-gtk"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # tests need x11
    "-Dvapi=true", "-Dman=true", "-Dtests=false", "-Ddocs=false",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "vala-devel", "glib-devel",
    "xsltproc", "docbook-xsl",
]
makedepends = ["colord-devel", "gtk+3-devel"]
pkgdesc = "Gtk+ support library for colord"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/colord-gtk"
source = f"$(FREEDESKTOP_SITE)/colord/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "2a4cfae08bc69f000f40374934cd26f4ae86d286ce7de89f1622abc59644c717"

@subpackage("colord-gtk-devel")
def _devel(self):
    return self.default_devel()
