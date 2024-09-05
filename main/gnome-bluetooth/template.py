pkgname = "gnome-bluetooth"
pkgver = "47_rc"
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
source = f"$(GNOME_SITE)/gnome-bluetooth/{pkgver[:2]}/gnome-bluetooth-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "a805f205c05c4512a3994c6da3e9517c9573047b359f1e9f012faab799af7328"
options = ["!cross"]


@subpackage("gnome-bluetooth-devel")
def _(self):
    return self.default_devel()
