pkgname = "geoclue"
pkgver = "2.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddbus-srv-user=_geoclue",
    "-Dgtk-doc=false",
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Dsoup2=false",
    "-Ddemo-agent=false", # problematic meson.build
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala",
    "gettext-tiny",
]
makedepends = [
    "eudev-devel", "json-glib-devel", "libsoup-devel", "libnotify-devel",
    "modemmanager-devel", "avahi-glib-devel",
]
pkgdesc = "D-Bus geoinformation service"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/geoclue/geoclue/wikis/home"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "cdc9efcb98ce81284d7a6c3c899330481ffdca44bba3c18b9e530618298aa4a0"
# glib
hardening = ["!vis"]

system_users = ["_geoclue"]

@subpackage("geoclue-devel")
def _devel(self):
    return self.default_devel()
