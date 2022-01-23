pkgname = "gjs"
pkgver = "1.70.0_git20220121"
pkgrel = 0
# use a git commit for now for mozjs91 compatibility
_commit = "87d2609256681be990401aa3d9644b12752e3eea"
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
    "dbus-devel", "libglib-devel", "mozjs91-devel", "cairo-devel",
    "libedit-devel",
]
checkdepends = ["gir-freedesktop", "gtk+3"]
pkgdesc = "JavaScript bindings for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"{url}/-/archive/{_commit}.tar.gz"
sha256 = "be5eae656c17e8a870fc5fb2ac0fb07de89f04a96f3851aef2fec83033c327f8"

def post_install(self):
    self.install_license("COPYING")

@subpackage("gjs-devel")
def _devel(self):
    return self.default_devel()
