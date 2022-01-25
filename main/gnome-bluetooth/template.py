pkgname = "gnome-bluetooth"
pkgver = "3.34.5"
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
    "gtk+3-devel", "libnotify-devel", "libcanberra-devel", "eudev-devel"
]
checkdepends = ["python-dbus"]
depends = ["bluez"]
pkgdesc = "GNOME Bluetooth widgets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GnomeBluetooth"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6c949e52c8becc2054daacd604901f66ce5cf709a5fa91c4bb7cacc939b53ea9"

@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
