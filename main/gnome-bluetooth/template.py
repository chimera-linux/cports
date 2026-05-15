pkgname = "gnome-bluetooth"
pkgver = "47.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "gsound-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libcanberra-devel",
    "libnotify-devel",
    "udev-devel",
    "upower-devel",
]
checkdepends = ["python-dbus"]
depends = ["bluez"]
pkgdesc = "GNOME Bluetooth widgets"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GnomeBluetooth"
source = f"$(GNOME_SITE)/gnome-bluetooth/{pkgver[:-2]}/gnome-bluetooth-{pkgver}.tar.xz"
sha256 = "41f20e6d6176b72590af63552b232d83f2fffdd77ecfaa5eaf32c5a4a86fad64"
options = ["!cross"]


@subpackage("gnome-bluetooth-devel")
def _(self):
    return self.default_devel()
