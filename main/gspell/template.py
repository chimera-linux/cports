pkgname = "gspell"
pkgver = "1.9.1"
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
sha256 = "dcbb769dfdde8e3c0a8ed3102ce7e661abbf7ddf85df08b29915e92cd723abdd"
# needs graphical env
options = ["!check"]

@subpackage("gspell-devel")
def _devel(self):
    return self.default_devel()
