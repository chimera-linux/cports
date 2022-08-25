pkgname = "gnome-bluetooth"
pkgver = "42.3"
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
    "eudev-devel", "gsound-devel", "upower-devel",
]
checkdepends = ["python-dbus"]
depends = ["bluez"]
pkgdesc = "GNOME Bluetooth widgets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GnomeBluetooth"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c37a2a07f77d4816b261e6c2086a056ed9767c3881dfabc826f4f82f6e1aa302"
options = ["!cross"]

@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
