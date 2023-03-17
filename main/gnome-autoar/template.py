pkgname = "gnome-autoar"
pkgver = "0.4.4"
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
sha256 = "c0afbe333bcf3cb1441a1f574cc8ec7b1b8197779145d4edeee2896fdacfc3c2"
options = ["!cross"]

@subpackage("gnome-autoar-devel")
def _devel(self):
    return self.default_devel()
