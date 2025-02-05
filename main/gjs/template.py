pkgname = "gjs"
pkgver = "1.82.1"
pkgrel = 0
build_style = "meson"
# disable tests that need X/dbus
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dskip_dbus_tests=true",
    "-Dskip_gtk_tests=true",
    "-Dinstalled_tests=false",
    "-Dprofiler=disabled",
    "-Db_ndebug=true",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "glib-devel",
    "libedit-readline-devel",
    "mozjs128-devel",
]
checkdepends = ["gobject-introspection-freedesktop", "gtk+3"]
pkgdesc = "JavaScript bindings for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"$(GNOME_SITE)/gjs/{pkgver[:-2]}/gjs-{pkgver}.tar.xz"
sha256 = "fb39aa5636576de0e5a1171f56a1a5825e2bd1a69972fb120ba78bd109b5693c"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    # seemingly ignores the configure arg
    self.uninstall("usr/lib/installed-tests")


@subpackage("gjs-devel")
def _(self):
    return self.default_devel()
