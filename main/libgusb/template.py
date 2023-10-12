pkgname = "libgusb"
pkgver = "0.4.7"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "glib-devel",
    "libusb-devel",
    "libgudev-devel",
    "json-glib-devel",
    "vala-devel",
    "usbutils",
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8acdd015c6f572555f8ec54c045e2d340baeb08468f6be519369c713794234f7"
# no access to usb in container
options = ["!check", "!cross"]


@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()
