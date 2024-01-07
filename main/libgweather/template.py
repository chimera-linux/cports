pkgname = "libgweather"
pkgver = "4.4.0"
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
sha256 = "366e866ff2a708b894cfea9475b8e8ff54cb3e2b477ea72a8ade0dabee5f48a4"
# needs network access
options = ["!check"]


@subpackage("libgweather-devel")
def _devel(self):
    return self.default_devel()
