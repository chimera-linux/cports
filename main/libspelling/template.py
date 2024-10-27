pkgname = "libspelling"
pkgver = "0.4.4"
pkgrel = 1
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
sha256 = "ece954588e6b86cc6a6c05904907cccf1a0fc2d08ebd030d66d8c6470a8c3463"
# introspection
options = ["!cross"]


@subpackage("libspelling-devel")
def _(self):
    return self.default_devel()
