pkgname = "gspell"
pkgver = "1.12.0"
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
    "glib-devel", "enchant-devel", "gtk+3-devel", "icu-devel", "vala"
]
pkgdesc = "Spell-checking library for Gtk+"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gspell"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "40d2850f1bb6e8775246fa1e39438b36caafbdbada1d28a19fa1ca07e1ff82ad"
# needs graphical env
options = ["!check"]

@subpackage("gspell-devel")
def _devel(self):
    return self.default_devel()
