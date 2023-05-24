pkgname = "geoclue"
pkgver = "2.7.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddbus-srv-user=_geoclue",
    "-Dgtk-doc=false",
    "-Dintrospection=true",
    "-Dvapi=true",
    "-Ddemo-agent=false",  # problematic meson.build
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
    "gettext-tiny",
]
makedepends = [
    "udev-devel",
    "json-glib-devel",
    "libsoup-devel",
    "libnotify-devel",
    "modemmanager-devel",
    "avahi-glib-devel",
]
pkgdesc = "D-Bus geoinformation service"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/geoclue/geoclue/wikis/home"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "1dce8e573cd338bc87a5bd725f89a6f543fac838e2a5d832515cb5ea0d86cf40"

system_users = ["_geoclue"]


@subpackage("geoclue-devel")
def _devel(self):
    return self.default_devel()
