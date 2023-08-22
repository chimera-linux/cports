pkgname = "libgsf"
pkgver = "1.14.50"
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
sha256 = "6e6c20d0778339069d583c0d63759d297e817ea10d0d897ebbe965f16e2e8e52"


@subpackage("libgsf-devel")
def _devel(self):
    return self.default_devel()
