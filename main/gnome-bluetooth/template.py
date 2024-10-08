pkgname = "gnome-bluetooth"
pkgver = "47.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "libxml2-progs",
    "gettext",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "libnotify-devel",
    "libcanberra-devel",
    "udev-devel",
    "gsound-devel",
    "upower-devel",
]
checkdepends = ["python-dbus"]
depends = ["bluez"]
pkgdesc = "GNOME Bluetooth widgets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GnomeBluetooth"
source = f"$(GNOME_SITE)/gnome-bluetooth/{pkgver[:-2]}/gnome-bluetooth-{pkgver}.tar.xz"
sha256 = "03e3e7403a15108ffc1496210a1da5c2961b2834a5c07eccc7a3f493195daba3"
options = ["!cross"]


@subpackage("gnome-bluetooth-devel")
def _(self):
    return self.default_devel()
