pkgname = "telepathy-glib"
pkgver = "0.24.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-vala-bindings"]
hostmakedepends = ["automake", "pkgconf", "libtool", "gtk-doc-tools", "vala"]
makedepends = [
    "dbus-devel",
    "dbus-glib-devel",
    "glib-devel",
    "gobject-introspection",
]
checkdepends = ["dbus"]
pkgdesc = "GLib bindings for the Telepathy D-Bus protocol"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause"
url = "https://github.com/TelepathyIM/telepathy-glib"
source = f"{url}/archive/refs/tags/telepathy-glib-{pkgver}.tar.gz"
sha256 = "a66451318d5bb5233a798bb4f73e16f1d886b97acff666efbefd9506d89875a2"


def post_install(self):
    self.install_license("COPYING")


@subpackage("telepathy-glib-devel")
def _(self):
    return self.default_devel()
