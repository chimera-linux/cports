pkgname = "libgweather"
# use devel snapshot for now for libsoup3 support
pkgver = "3.91.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsoup2=false", "-Dgtk_doc=false", "-Denable_vala=true",
    "-Dzoneinfo_dir=/usr/share/zoneinfo",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "gettext-tiny", "vala", "python-gobject-devel"
]
makedepends = [
    "geocode-glib-devel", "gtk+3-devel", "libsoup-devel"
]
depends = ["tzdata"]
pkgdesc = "GNOME Weather information access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/LibGWeather"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "725b3eb34fc6d21edc80b6e684728b3088b1fa144f0a2a4d3e9605c7a8f3dcf8"
# glib
hardening = ["!vis"]
# needs network access
options = ["!check"]

@subpackage("libgweather-devel")
def _devel(self):
    return self.default_devel()
