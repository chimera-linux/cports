pkgname = "gnome-autoar"
pkgver = "0.4.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled", "-Dvapi=true", "-Dtests=true", "-Dgtk_doc=true",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "gtk-doc-tools",
    "gobject-introspection",
]
makedepends = ["gtk+3-devel", "libarchive-devel"]
pkgdesc = "Archiving functions and widgets for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-autoar"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "7bdf0789553496abddc3c963b0ce7363805c0c02c025feddebcaacc787249e88"
# glib
hardening = ["!vis"]
options = ["!cross"]

@subpackage("gnome-autoar-devel")
def _devel(self):
    return self.default_devel()
