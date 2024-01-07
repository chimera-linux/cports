pkgname = "gnome-bluetooth"
pkgver = "42.7"
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
sha256 = "94df1729dbec3bb105e588eaf5312bbbaa05c49ea733202a10dc3f7532bdf869"
options = ["!cross"]


@subpackage("gnome-bluetooth-devel")
def _devel(self):
    return self.default_devel()
