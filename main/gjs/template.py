pkgname = "gjs"
pkgver = "1.84.1"
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
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"$(GNOME_SITE)/gjs/{pkgver[:-2]}/gjs-{pkgver}.tar.xz"
sha256 = "44796b91318dbbe221a13909f00fd872ef92f38c68603e0e3574e46bc6bac32c"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    # seemingly ignores the configure arg
    self.uninstall("usr/lib/installed-tests")


@subpackage("gjs-devel")
def _(self):
    return self.default_devel()
