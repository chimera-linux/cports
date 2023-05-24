pkgname = "amtk"
pkgver = "5.6.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext-tiny",
]
makedepends = ["glib-devel", "gtk+3-devel"]
pkgdesc = "Actions, Menus and Toolbars Kit for GTK+ applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/World/amtk"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d50115b85c872aac296934b5ee726a3fa156c6f5ad96d27e0edd0aa5ad173228"


@subpackage("amtk-devel")
def _devel(self):
    return self.default_devel()
