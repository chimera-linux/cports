pkgname = "gnome-bluetooth"
pkgver = "42.5"
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
sha256 = "a4f5f1ac2dbb7b7b92f7d6d2b42c030f62aed9b5426b9dc116946041f3cba8f7"
options = ["!cross"]

@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
