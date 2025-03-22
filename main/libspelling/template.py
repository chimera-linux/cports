pkgname = "libspelling"
pkgver = "0.4.7"
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
sha256 = "421fb9df07c78bb7e2db765e3a9ff5122b67dfdec4bbf0c71b9b849be0f84914"
# introspection
options = ["!cross"]


@subpackage("libspelling-devel")
def _(self):
    return self.default_devel()
