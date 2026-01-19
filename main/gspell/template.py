pkgname = "gspell"
pkgver = "1.14.1"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gspell"
source = f"https://gitlab.gnome.org/GNOME/gspell/-/archive/{pkgver}/gspell-{pkgver}.tar.gz"
sha256 = "1ecdc789e4f798e63cf49fc1718541e7974e5f67034ce152ae052a2b8f337e8e"
# check: needs seatful headless
# cross: gobject-introspection
options = ["!check", "!cross"]


@subpackage("gspell-devel")
def _(self):
    return self.default_devel()
