pkgname = "gspell"
pkgver = "1.14.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dgtk_doc=false", "-Dinstall_tests=false"]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "enchant-devel",
    "glib-devel",
    "gtk+3-devel",
    "icu-devel",
    "vala",
]
pkgdesc = "Spell-checking library for Gtk+"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gspell"
source = f"$(GNOME_SITE)/gspell/{pkgver[:-2]}/gspell-{pkgver}.tar.xz"
sha256 = "64ea1d8e9edc1c25b45a920e80daf67559d1866ffcd7f8432fecfea6d0fe8897"
# check: needs seatful headless
# cross: gobject-introspection
options = ["!check", "!cross"]


@subpackage("gspell-devel")
def _(self):
    return self.default_devel()
