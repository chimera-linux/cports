pkgname = "dbus-glib"
pkgver = "0.112"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "gtk-doc-tools", "pkgconf"]
makedepends = [
    "dbus-devel",
    "glib-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Deprecated library for D-Bus IPC"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AFL-2.1"
url = "https://dbus.freedesktop.org"
source = f"{url}/releases/dbus-glib/dbus-glib-{pkgver}.tar.gz"
sha256 = "7d550dccdfcd286e33895501829ed971eeb65c614e73aadb4a08aeef719b143a"


@subpackage("dbus-glib-libs")
def _(self):
    return self.default_libs()


@subpackage("dbus-glib-devel")
def _(self):
    return self.default_devel()
