pkgname = "gnome-bluetooth"
pkgver = "42.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true", "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "libxml2-progs",
    "gettext-tiny",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "libnotify-devel", "libcanberra-devel",
    "udev-devel", "gsound-devel", "upower-devel",
]
checkdepends = ["python-dbus"]
depends = ["bluez"]
pkgdesc = "GNOME Bluetooth widgets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GnomeBluetooth"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1d6fcf1cdb6cc9923ab334a2c0bc37a2c1bba9d18de153d484eedc04f3c0bcdc"
options = ["!cross"]

@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
