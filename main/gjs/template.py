pkgname = "gjs"
pkgver = "1.88.0"
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
checkdepends = ["bash", "gobject-introspection-freedesktop", "gtk+3"]
pkgdesc = "JavaScript bindings for GNOME"
license = "MIT OR LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gjs"
source = f"$(GNOME_SITE)/gjs/{pkgver[:-2]}/gjs-{pkgver}.tar.xz"
sha256 = "30a0b9f3317e8e60b1896db2903c70e8b0cd33df953c328755803a75191dc453"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    # seemingly ignores the configure arg
    self.uninstall("usr/lib/installed-tests")


@subpackage("gjs-devel")
def _(self):
    return self.default_devel()
