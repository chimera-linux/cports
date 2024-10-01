pkgname = "libgsf"
pkgver = "1.14.53"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-introspection"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["gdk-pixbuf-devel", "libxml2-devel"]
checkdepends = ["perl-xml-parser", "unzip"]
pkgdesc = "Structured File Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libgsf"
source = f"$(GNOME_SITE)/libgsf/{pkgver[:-3]}/libgsf-{pkgver}.tar.xz"
sha256 = "0eb59a86e0c50f97ac9cfe4d8cc1969f623f2ae8c5296f2414571ff0a9e8bcba"


@subpackage("libgsf-devel")
def _(self):
    return self.default_devel()
