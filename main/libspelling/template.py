pkgname = "libspelling"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Denchant=enabled",
    "-Dsysprof=false",
    "-Dvapi=true",
]
hostmakedepends = [
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
sha256 = "92ef62dca817c7d6ddbd0b6a0eb4f5ea5725b3211547de9321dcbfe3ef9707d3"
# introspection
options = ["!cross"]


@subpackage("libspelling-devel")
def _(self):
    return self.default_devel()
