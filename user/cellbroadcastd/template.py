pkgname = "cellbroadcastd"
pkgver = "0.0.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gmobile-devel",
    "gobject-introspection-devel",
    "mobile-broadband-provider-info",
    "modemmanager-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Manages cell broadcast messages received via ModemManager"
license = "LGPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/devrtz/cellbroadcastd"
source = f"https://sources.phosh.mobi/releases/cellbroadcastd/cellbroadcastd-{pkgver}.tar.xz"
sha256 = "686d44cd02e23efaade0d28ea3f34d96562d856db6776fd0af4dbc0fe3a30392"


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("cellbroadcastd-devel")
def _(self):
    return self.default_devel()
