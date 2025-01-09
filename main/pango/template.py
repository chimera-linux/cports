pkgname = "pango"
pkgver = "1.54.0"
pkgrel = 4
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
sha256 = "8a9eed75021ee734d7fc0fdf3a65c3bba51dfefe4ae51a9b414a60c70b2d1ed8"
# subtly breaks various things
hardening = ["!int"]


@subpackage("pango-xft")
def _(self):
    self.subdesc = "X font rendering"

    return ["usr/lib/libpangoxft*.so.*"]


@subpackage("pango-view")
def _(self):
    self.subdesc = "utility to view pango files"

    return ["usr/bin/pango-view", "usr/share/man/man1/pango-view.1"]


@subpackage("pango-devel")
def _(self):
    return self.default_devel()
