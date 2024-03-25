pkgname = "gnome-bluetooth"
pkgver = "46.0"
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "13fe1e75f317acdbdf5e80c9029d2e0632d60a9ccf72a43ae36eb7545021fbef"
options = ["!cross"]


@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
