pkgname = "geoclue"
pkgver = "2.8.2"
pkgrel = 0
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
sha256 = "d4d65933b704d4c8d4ca9747dc511b883e35099abe534c8560f2aab3017e4cd4"
options = ["etcfiles"]


def post_install(self):
    self.install_sysusers(self.files_path / "geoclue.conf")
    self.uninstall("usr/lib/sysusers.d/geoclue-sysusers.conf")


@subpackage("geoclue-devel")
def _(self):
    return self.default_devel()
