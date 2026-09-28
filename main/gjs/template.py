pkgname = "gjs"
pkgver = "1.90.0"
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
sha256 = "47e9f22b1d4aca841c6c492b449b6de32ff680972183e26fe7b98a45c5c3fee1"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    # seemingly ignores the configure arg
    self.uninstall("usr/lib/installed-tests")


@subpackage("gjs-devel")
def _(self):
    return self.default_devel()
