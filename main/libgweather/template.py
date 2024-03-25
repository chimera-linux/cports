pkgname = "libgweather"
pkgver = "4.4.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsoup2=false",
    "-Dgtk_doc=false",
    "-Denable_vala=true",
    "-Dzoneinfo_dir=/usr/share/zoneinfo",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext",
    "vala",
    "python-gobject-devel",
]
makedepends = [
    "geocode-glib-devel",
    "libsoup-devel",
    "libxml2-devel",
    "json-glib-devel",
]
depends = ["tzdata"]
pkgdesc = "GNOME Weather information access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/LibGWeather"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a6e427b4770ada48945f3aa906af710fc833cff0d42df91f1828302740d794ec"
# needs network access
options = ["!check"]


@subpackage("libgweather-devel")
def _devel(self):
    return self.default_devel()
