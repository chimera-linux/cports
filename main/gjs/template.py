pkgname = "gjs"
pkgver = "1.74.2"
pkgrel = 0
build_style = "meson"
# disable tests that need X/dbus
configure_args = [
    "-Dskip_dbus_tests=true", "-Dskip_gtk_tests=true",
    "-Dinstalled_tests=false", "-Dprofiler=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
]
makedepends = [
    "dbus-devel", "libglib-devel", "mozjs102-devel", "cairo-devel",
    "libedit-readline-devel",
]
checkdepends = ["gir-freedesktop", "gtk+3"]
pkgdesc = "JavaScript bindings for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "56597b638827ca3c46e1880617398d4a0a70c59781b79a7e04beaec3499a7d7c"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("gjs-devel")
def _devel(self):
    return self.default_devel()
