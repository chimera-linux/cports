pkgname = "gjs"
pkgver = "1.74.1"
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
sha256 = "c5e0b762a3740424a6ef5802606867f6456c6473118de09a4fa9b5186aa11f43"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("gjs-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
