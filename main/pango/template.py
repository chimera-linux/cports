pkgname = "pango"
pkgver = "1.50.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "help2man", "gobject-introspection",
]
makedepends = [
    "fribidi-devel", "harfbuzz-devel", "libxft-devel", "libthai-devel",
    "cairo-devel",
]
checkdepends = [
    "fonts-dejavu-ttf", "fonts-liberation-ttf", "fonts-cantarell-otf"
]
pkgdesc = "Text rendering and layout library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.pango.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1b636aabf905130d806372136f5e137b6a27f26d47defd9240bf444f6a4fe610"

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
