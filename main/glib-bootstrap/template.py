pkgname = "glib-bootstrap"
pkgver = "2.82.4"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Ddocumentation=false",
    "-Dintrospection=disabled",
    "-Dman-pages=disabled",
    "-Dselinux=disabled",
    "-Dtests=false",
]
hostmakedepends = [
    "meson",
    "gettext",
    "pkgconf",
    "python-packaging",
]
makedepends = [
    "dbus-devel",
    "elfutils-devel",
    "libffi8-devel",
    "pcre2-devel",
    "util-linux-mount-devel",
    "zlib-ng-compat-devel",
]
depends = ["!glib", "!glib-devel"]
provides = [
    "so:libgio-2.0.so.0=0",
    "so:libglib-2.0.so.0=0",
    "so:libgmodule-2.0.so.0=0",
    "so:libgobject-2.0.so.0=0",
    "so:libgthread-2.0.so.0=0",
]
pkgdesc = "GLib library of C routines"
subdesc = "bootstrap"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/glib/{pkgver[:-2]}/glib-{pkgver}.tar.xz"
sha256 = "37dd0877fe964cd15e9a2710b044a1830fb1bd93652a6d0cb6b8b2dff187c709"
# FIXME int - strfuncs failure
hardening = ["!int"]
# bootstrap only
options = ["!check", "!lto", "!scanshlibs", "!autosplit"]


def post_install(self):
    self.install_license("COPYING")
