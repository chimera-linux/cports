pkgname = "colord-gtk"
pkgver = "0.3.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # tests need x11
    "-Dvapi=true",
    "-Dman=true",
    "-Dtests=false",
    "-Ddocs=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala-devel",
    "glib-devel",
    "xsltproc",
    "docbook-xsl",
]
makedepends = ["colord-devel", "gtk4-devel", "gtk+3-devel"]
pkgdesc = "Gtk+ support library for colord"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/colord-gtk"
source = f"$(FREEDESKTOP_SITE)/colord/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "b9466656d66d9a6ffbc2dd04fa91c8f6af516bf9efaacb69744eec0f56f3c1d0"
options = ["!cross"]


@subpackage("colord-gtk-devel")
def _devel(self):
    return self.default_devel()
