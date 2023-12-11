pkgname = "libspelling"
pkgver = "0.2.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Denchant=enabled", "-Dvapi=true", "-Ddocs=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
    "glib-devel",
]
makedepends = [
    "enchant-devel",
    "glib-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "icu-devel",
]
pkgdesc = "Spellcheck library for GTK 4"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/chergert/libspelling"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ab8204d35b6b103193c525fe05e63e45f2825582055f113d3e5f5f8ff60bd144"


@subpackage("libspelling-devel")
def _devel(self):
    return self.default_devel()
