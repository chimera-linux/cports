pkgname = "json-glib"
pkgver = "1.10.8"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dinstalled_tests=false"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel"]
pkgdesc = "JSON parser for glib-based projects"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/action/show/Projects/JsonGlib"
source = f"$(GNOME_SITE)/json-glib/{pkgver[:-2]}/json-glib-{pkgver}.tar.xz"
sha256 = "55c5c141a564245b8f8fbe7698663c87a45a7333c2a2c56f06f811ab73b212dd"


@subpackage("json-glib-devel")
def _(self):
    return self.default_devel()
