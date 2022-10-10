pkgname = "gjs"
pkgver = "1.74.0"
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
sha256 = "859d45ecfe860473838b88e063cdf882a957017097e8ffc756b8862d1ebbb5a7"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("gjs-devel")
def _devel(self):
    return self.default_devel()
