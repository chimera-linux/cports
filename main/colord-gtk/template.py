pkgname = "colord-gtk"
pkgver = "0.3.1"
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
    "docbook-xsl",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala-devel",
    "libxslt-progs",
]
makedepends = ["colord-devel", "gtk4-devel", "gtk+3-devel"]
pkgdesc = "Gtk+ support library for colord"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/colord-gtk"
source = f"$(FREEDESKTOP_SITE)/colord/releases/colord-gtk-{pkgver}.tar.xz"
sha256 = "c176b889b75630a17f4e3d7ef24c09a3e12368e633496087459c8b53ac3a122d"
options = ["!cross"]


@subpackage("colord-gtk-devel")
def _(self):
    return self.default_devel()
