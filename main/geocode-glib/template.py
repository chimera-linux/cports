pkgname = "geocode-glib"
pkgver = "3.26.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-gtk-doc=false",
    "-Denable-installed-tests=false",
    "-Dsoup2=false",
    "-Denable-introspection=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
]
makedepends = [
    "json-glib-devel",
    "libsoup-devel",
]
pkgdesc = "GLib library for geocoding and reverse geocoding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://developer.gnome.org/geocode-glib"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2d9a6826d158470449a173871221596da0f83ebdcff98b90c7049089056a37aa"


@subpackage("geocode-glib-devel")
def _devel(self):
    return self.default_devel()
