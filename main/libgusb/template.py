pkgname = "libgusb"
pkgver = "0.3.10"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "libglib-devel", "libusb-devel", "libgudev-devel", "vala-devel", "usbutils"
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"http://people.freedesktop.org/~hughsient/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "0eb0b9ab0f8bba0c59631c809c37b616ef34eb3c8e000b0b9b71cf11e4931bdc"
# no access to usb in container
options = ["!check", "!cross"]

@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()
