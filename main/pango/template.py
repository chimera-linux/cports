pkgname = "pango"
pkgver = "1.56.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Dsysprof=enabled",
]
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
    "sysprof-capture",
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
source = (
    f"$(GNOME_SITE)/pango/{pkgver[: pkgver.rfind('.')]}/pango-{pkgver}.tar.xz"
)
sha256 = "426be66460c98b8378573e7f6b0b2ab450f6bb6d2ec7cecc33ae81178f246480"
# subtly breaks various things
hardening = ["!int"]


@subpackage("pango-xft")
def _(self):
    self.subdesc = "X font rendering"

    return ["usr/lib/libpangoxft*.so.*"]


@subpackage("pango-view")
def _(self):
    self.subdesc = "utility to view pango files"

    return ["cmd:pango-view"]


@subpackage("pango-devel")
def _(self):
    return self.default_devel()
