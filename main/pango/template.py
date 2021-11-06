pkgname = "pango"
_mver = "1.48"
pkgver = f"{_mver}.10"
pkgrel = 0
build_style = "meson"
# TODO: introspection
configure_args = ["-Dintrospection=disabled"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "help2man"]
makedepends = [
    "fribidi-devel", "harfbuzz-devel", "libxft-devel", "libthai-devel",
    "cairo-devel",
]
pkgdesc = "Text rendering and layout library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.pango.org"
source = f"$(GNOME_SITE)/{pkgname}/{_mver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "21e1f5798bcdfda75eabc4280514b0896ab56f656d4e7e66030b9a2535ecdc98"
# FIXME: missing checkdepends
options = ["!check"]

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
