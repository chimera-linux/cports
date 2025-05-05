pkgname = "libspelling"
pkgver = "0.4.8"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libspelling"
source = f"{url}/-/archive/{pkgver}/libspelling-{pkgver}.tar.gz"
sha256 = "6da9c8e1a0da49cc2a0e4b7837a87d8d818c96019feee5af1f2f9b698cf9b1de"
# introspection
options = ["!cross"]


@subpackage("libspelling-devel")
def _(self):
    return self.default_devel()
