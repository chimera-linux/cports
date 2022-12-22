pkgname = "libgusb"
pkgver = "0.4.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "libglib-devel", "libusb-devel", "libgudev-devel", "json-glib-devel",
    "vala-devel", "usbutils"
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"http://people.freedesktop.org/~hughsient/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "02d3a992a0cd16c46a346439334417617cd7cd5b2ccc5fe0fe998e9ffb8d5d8a"
# no access to usb in container
options = ["!check", "!cross"]

@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
