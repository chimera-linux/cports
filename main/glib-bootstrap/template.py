pkgname = "glib-bootstrap"
pkgver = "2.80.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dgtk_doc=false",
    "-Dintrospection=disabled",
    "-Dman=false",
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
    "libffi-devel",
    "libmount-devel",
    "pcre2-devel",
    "zlib-devel",
]
depends = ["!glib", "!glib-devel"]
provides = [
    "so:libgio-2.0.so.0=0",
    "so:libglib-2.0.so.0=0",
    "so:libgmodule-2.0.so.0=0",
    "so:libgobject-2.0.so.0=0",
    "so:libgthread-2.0.so.0=0",
]
pkgdesc = "GLib library of C routines (bootstrap)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/glib/{pkgver[:-2]}/glib-{pkgver}.tar.xz"
sha256 = "b9cfb6f7a5bd5b31238fd5d56df226b2dda5ea37611475bf89f6a0f9400fe8bd"
# FIXME int - strfuncs failure
hardening = ["!int"]
# bootstrap only
options = ["!check", "!lto", "!scanshlibs", "!autosplit"]


def post_install(self):
    self.install_license("COPYING")
