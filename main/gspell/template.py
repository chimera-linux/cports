pkgname = "gspell"
pkgver = "1.11.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--enable-introspection", "--enable-vala"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "gettext-tiny", "gobject-introspection",
    "vala", "glib-devel"
]
makedepends = [
    "libglib-devel", "enchant-devel", "gtk+3-devel", "icu-devel", "vala"
]
pkgdesc = "Spell-checking library for Gtk+"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gspell"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ef6aa4e3f711775158a7e241a5f809cf2426bc0e02c23a7d2b5c71fc3de00292"
# needs graphical env
options = ["!check"]

@subpackage("gspell-devel")
def _devel(self):
    return self.default_devel()
