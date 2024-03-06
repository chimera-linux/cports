pkgname = "pango"
pkgver = "1.52.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "help2man",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "fribidi-devel",
    "harfbuzz-devel",
    "libthai-devel",
    "libxft-devel",
]
checkdepends = [
    "fonts-cantarell-otf",
    "fonts-dejavu-ttf",
    "fonts-liberation-ttf",
]
pkgdesc = "Text rendering and layout library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.pango.org"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:pkgver.rfind('.')]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "58728a0a2d86f60761208df9493033d18ecb2497abac80ee1a274ad0c6e55f0f"


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
