pkgname = "libgweather"
pkgver = "4.4.4"
pkgrel = 1
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
depends = ["tzdb"]
pkgdesc = "GNOME Weather information access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/LibGWeather"
source = f"$(GNOME_SITE)/libgweather/{pkgver[:-2]}/libgweather-{pkgver}.tar.xz"
sha256 = "7017677753cdf7d1fdc355e4bfcdb1eba8369793a8df24d241427a939cbf4283"
# needs network access
options = ["!check"]


@subpackage("libgweather-devel")
def _(self):
    return self.default_devel()
