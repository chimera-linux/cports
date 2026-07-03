pkgname = "geoclue"
pkgver = "2.8.1"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Ddbus-srv-user=_geoclue",
    "-Dgtk-doc=false",
    "-Dintrospection=true",
    "-Dvapi=true",
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
sha256 = "1b5de03936bd8c031a1f6207c1857fa25a9aa1453ffe742f32a0a4a3281f2629"
options = ["etcfiles"]


def post_install(self):
    self.install_sysusers(self.files_path / "geoclue.conf")
    self.uninstall("usr/lib/sysusers.d/geoclue-sysusers.conf")


@subpackage("geoclue-devel")
def _(self):
    return self.default_devel()
