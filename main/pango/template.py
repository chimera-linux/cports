pkgname = "pango"
pkgver = "1.51.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "help2man",
    "gobject-introspection",
]
makedepends = [
    "fribidi-devel",
    "harfbuzz-devel",
    "libxft-devel",
    "libthai-devel",
    "cairo-devel",
]
checkdepends = [
    "fonts-dejavu-ttf",
    "fonts-liberation-ttf",
    "fonts-cantarell-otf",
]
pkgdesc = "Text rendering and layout library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.pango.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:pkgver.rfind('.')]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3dba407f2b5fc117e192f3025f0a1cc8edc1fd9b934b1c578b2b97342139415a"


@subpackage("pango-xft")
def _xft(self):
    self.pkgdesc = f"{pkgdesc} (X font rendering)"

    return ["usr/lib/libpangoxft*.so.*"]


@subpackage("pango-view")
def _view(self):
    self.pkgdesc = f"{pkgdesc} (utility to view pango files)"

    return ["usr/bin/pango-view", "usr/share/man/man1/pango-view.1"]


@subpackage("pango-devel")
def _devel(self):
    return self.default_devel()
