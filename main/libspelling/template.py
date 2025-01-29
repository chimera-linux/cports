pkgname = "libspelling"
pkgver = "0.4.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Denchant=enabled",
    "-Dsysprof=false",
    "-Dvapi=true",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "enchant-devel",
    "glib-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "icu-devel",
]
# any lang
checkdepends = ["aspell-en"]
pkgdesc = "Spellcheck library for GTK 4"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libspelling"
source = f"{url}/-/archive/{pkgver}/libspelling-{pkgver}.tar.gz"
sha256 = "ba7584b3b686bdab56aa156b33effdd03520451b51cddf18d1c836120fa2030a"
# introspection
options = ["!cross"]


@subpackage("libspelling-devel")
def _(self):
    return self.default_devel()
