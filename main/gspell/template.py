pkgname = "gspell"
pkgver = "1.12.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static", "--enable-introspection", "--enable-vala"]
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "gettext",
    "gobject-introspection",
    "vala",
    "glib-devel",
]
makedepends = [
    "glib-devel",
    "enchant-devel",
    "gtk+3-devel",
    "icu-devel",
    "vala",
]
pkgdesc = "Spell-checking library for Gtk+"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gspell"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b4e993bd827e4ceb6a770b1b5e8950fce3be9c8b2b0cbeb22fdf992808dd2139"
# needs graphical env
options = ["!check"]


@subpackage("gspell-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
