pkgname = "gjs"
pkgver = "1.86.0"
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
    "mozjs140-devel",
]
checkdepends = ["gobject-introspection-freedesktop", "gtk+3"]
pkgdesc = "JavaScript bindings for GNOME"
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"$(GNOME_SITE)/gjs/{pkgver[:-2]}/gjs-{pkgver}.tar.xz"
sha256 = "63448f7a57804d4c2a8d0c7f5e90e224d04d4eb2d560142c076c65a8eda00799"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    # seemingly ignores the configure arg
    self.uninstall("usr/lib/installed-tests")


@subpackage("gjs-devel")
def _(self):
    return self.default_devel()
