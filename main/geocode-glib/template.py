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
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "json-glib-devel",
    "libsoup-devel",
]
pkgdesc = "GLib library for geocoding and reverse geocoding"
license = "LGPL-2.1-or-later"
url = "https://developer.gnome.org/geocode-glib"
source = (
    f"$(GNOME_SITE)/geocode-glib/{pkgver[:-2]}/geocode-glib-{pkgver}.tar.xz"
)
sha256 = "2d9a6826d158470449a173871221596da0f83ebdcff98b90c7049089056a37aa"


@subpackage("geocode-glib-devel")
def _(self):
    return self.default_devel()
