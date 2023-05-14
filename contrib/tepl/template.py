pkgname = "tepl"
pkgver = "6.4.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "gettext-tiny",
]
makedepends = [
    "glib-devel", "gtk+3-devel", "amtk-devel", "gtksourceview4-devel",
    "libxml2-devel", "uchardet-devel", "gsettings-desktop-schemas-devel",
]
pkgdesc = "Text editor product line"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/swilmet/tepl"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5e56b20669d0cf05fa1d64b58c8c342c59158122dc518100d093d59df9b87321"
# needs graphical environment
options = ["!check", "!cross"]

@subpackage("tepl-devel")
def _devel(self):
    return self.default_devel()
