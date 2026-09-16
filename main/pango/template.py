pkgname = "pango"
pkgver = "1.58.2"
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
license = "LGPL-2.1-or-later"
url = "https://www.pango.org"
source = (
    f"$(GNOME_SITE)/pango/{pkgver[: pkgver.rfind('.')]}/pango-{pkgver}.tar.xz"
)
sha256 = "342385b6ca3b7c73455d7c80a13b7dbe4489e00bc3bd4c5bd6ed4dce421e374a"
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
