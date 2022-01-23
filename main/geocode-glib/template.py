pkgname = "geocode-glib"
pkgver = "3.26.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-gtk-doc=false", "-Denable-installed-tests=false",
    "-Dsoup2=false", "-Denable-introspection=true",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
]
makedepends = [
    "json-glib-devel", "libsoup-devel",
]
pkgdesc = "GLib library for geocoding and reverse geocoding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://developer.gnome.org/geocode-glib"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "01fe84cfa0be50c6e401147a2bc5e2f1574326e2293b55c69879be3e82030fd1"

@subpackage("geocode-glib-devel")
def _devel(self):
    return self.default_devel()
