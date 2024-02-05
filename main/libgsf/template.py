pkgname = "libgsf"
pkgver = "1.14.52"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "gettext-devel",
    "glib-devel",
    "gtk-doc-tools",
    "gobject-introspection",
    "automake",
    "libtool",
]
makedepends = ["gdk-pixbuf-devel", "libxml2-devel"]
checkdepends = ["perl-xml-parser", "unzip"]
pkgdesc = "Structured File Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libgsf"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "9181c914b9fac0e05d6bcaa34c7b552fe5fc0961d3c9f8c01ccc381fb084bcf0"


@subpackage("libgsf-devel")
def _devel(self):
    return self.default_devel()
