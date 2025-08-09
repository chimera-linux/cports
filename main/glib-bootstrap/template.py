pkgname = "glib-bootstrap"
pkgver = "2.84.4"
pkgrel = 0
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
    "gettext",
    "meson",
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
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/glib/{pkgver[:-2]}/glib-{pkgver}.tar.xz"
sha256 = "8a9ea10943c36fc117e253f80c91e477b673525ae45762942858aef57631bb90"
# FIXME int - strfuncs failure
hardening = ["!int"]
# bootstrap only
options = ["!check", "!lto", "!scanshlibs", "!autosplit"]


def post_install(self):
    self.install_license("COPYING")
