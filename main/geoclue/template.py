pkgname = "geoclue"
pkgver = "2.7.1"
pkgrel = 1
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
    "gettext",
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
source = f"https://gitlab.freedesktop.org/geoclue/geoclue/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "5624cd41148643c46d681d39153c7d26fdb8831e7e7c8601c300732fa8a6db1c"


def post_install(self):
    self.install_file(self.files_path / "geoclue.conf", "usr/lib/sysusers.d")


@subpackage("geoclue-devel")
def _devel(self):
    return self.default_devel()
