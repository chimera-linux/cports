pkgname = "gnome-bluetooth"
pkgver = "46.1"
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
sha256 = "56c44a17034598e9607458afae1be75f3de5efdf0e62355f09ba58fc7bc312ac"
options = ["!cross"]


@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
