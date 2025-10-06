pkgname = "geoclue"
pkgver = "2.8.0"
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
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "avahi-glib-devel",
    "json-glib-devel",
    "libnotify-devel",
    "libsoup-devel",
    "modemmanager-devel",
    "udev-devel",
]
pkgdesc = "D-Bus geoinformation service"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/geoclue/geoclue/wikis/home"
source = f"https://gitlab.freedesktop.org/geoclue/geoclue/-/archive/{pkgver}/geoclue-{pkgver}.tar.bz2"
sha256 = "c07aeb35cccf959ec1dc2e8f9a71a9d8bdd643879ef0a8d37926499541da1685"


def post_install(self):
    self.install_sysusers(self.files_path / "geoclue.conf")


@subpackage("geoclue-devel")
def _(self):
    return self.default_devel()
