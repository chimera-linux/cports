pkgname = "libspelling"
pkgver = "0.2.1"
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
url = "https://gitlab.gnome.org/GNOME/libspelling"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "413b22a358e77f2302d15a8fbd3ed4ad8fdecea38dfd5c687af4c567c6b3e15a"


@subpackage("libspelling-devel")
def _devel(self):
    return self.default_devel()
