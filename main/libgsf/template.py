pkgname = "libgsf"
pkgver = "1.14.49"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-introspection"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "gettext-tiny-devel", "glib-devel",
    "gobject-introspection"
]
makedepends = ["gdk-pixbuf-devel", "libxml2-devel"]
checkdepends = ["perl-xml-parser", "unzip"]
pkgdesc = "Structured File Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libgsf"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e9ebe36688f010c9e6e40c8903f3732948deb8aca032578d07d0751bd82cf857"

@subpackage("libgsf-devel")
def _devel(self):
    return self.default_devel()
