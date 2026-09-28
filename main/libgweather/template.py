pkgname = "libgweather"
pkgver = "4.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgtk_doc=false",
    "-Denable_vala=true",
    "-Dzoneinfo_dir=/usr/share/zoneinfo",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-gobject-devel",
    "vala",
]
makedepends = [
    "geocode-glib-devel",
    "gweather-locations-devel",
    "json-glib-devel",
    "libsoup-devel",
    "libxml2-devel",
]
depends = ["gweather-locations", "tzdb"]
pkgdesc = "GNOME Weather information access library"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/LibGWeather"
source = f"$(GNOME_SITE)/libgweather/{pkgver[:-2]}/libgweather-{pkgver}.tar.xz"
sha256 = "7f5d0e8c9685ef2ff46c2f3a57cae48d7bf3540b2d83921f889ef28e6a876788"
# needs network access
options = ["!check"]


@subpackage("libgweather-devel")
def _(self):
    return self.default_devel()
