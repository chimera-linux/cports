pkgname = "gjs"
pkgver = "1.78.0"
pkgrel = 0
build_style = "meson"
# disable tests that need X/dbus
configure_args = [
    "-Dskip_dbus_tests=true",
    "-Dskip_gtk_tests=true",
    "-Dinstalled_tests=false",
    "-Dprofiler=disabled",
    "-Db_ndebug=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "mozjs115-devel",
    "cairo-devel",
    "libedit-readline-devel",
]
checkdepends = ["gir-freedesktop", "gtk+3"]
pkgdesc = "JavaScript bindings for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "91be2ebcab6707e2d8301d4e261530a9b1d55082f5d7746ba0f978e2efb712f5"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("gjs-devel")
def _devel(self):
    return self.default_devel()
